// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.

// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.

// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.

//WeShareGold issued by WeShareChain! http://www.wesharechain.net

// Standard token interface (ERC 20)
// https://github.com/ethereum/EIPs/issues/20
//contract ERC20 {
//   function totalSupply() constant returns (uint theTotalSupply);
//   function balanceOf(address _owner) constant returns (uint balance);
//   function transfer(address _to, uint _value) returns (bool success);
//   function transferFrom(address _from, address _to, uint _value) returns (bool success);
//   function approve(address _spender, uint _value) returns (bool success);
//   function allowance(address _owner, address _spender) constant returns (uint remaining);
//   event Transfer(address indexed _from, address indexed _to, uint _value);
//   event Approval(address indexed _owner, address indexed _spender, uint _value);
//}


pragma solidity ^0.4.25;
 
interface tokenRecipient { function receiveApproval(address _from, uint256 _value, address _token, bytes _extraData) public; }
 
contract TokenERC20 {
    string public name = "We Share Gold"; // 加密数字黄金
    string public symbol = "WSG"; // WSG
    uint8 public decimals = 5;  // 
    uint256 public totalSupply = 1600000000; // 总供应量16亿
 
    // 余额
    mapping (address => uint256) public balanceOf;
    // 存储对账号的控制，控制加密数字黄金的交易，如可交易账号及资产
    mapping (address => mapping (address => uint256)) public allowance;
 
    // 用来通知客户端交易发生的事件
    event Transfer(address indexed from, address indexed to, uint256 value);
 
    // 用来通知客户端加密数字黄金被消费的事件
    event Burn(address indexed from, uint256 value);
 
    // 用来通知客户端锁定的事件
    event Freeze(address indexed from, uint256 value);
 
    // 用来通知客户端锁定的事件
    event Unfreeze(address indexed from, uint256 value);

    /**
     * 初始化构造
     */
    function TokenERC20(uint256 initialSupply, string tokenName, string tokenSymbol) public {
        totalSupply = initialSupply * 10 ** uint256(decimals);  // 供应的份额，份额跟最小的加密数字黄金单位有关，份额 = 币数 * 10 ** decimals。
        balanceOf[msg.sender] = totalSupply;                // 总供应量
        name = tokenName;                                   // 加密数字黄金
        symbol = tokenSymbol;                               // WST
    }

    /**
     * 加密数字黄金交易内部封装接口
     */
    function _transfer(address _from, address _to, uint _value) internal {
        // 确保目标地址不为0x0，因为0x0地址代表销毁
        require(_to != 0x0);
        // 检查发送者余额
        require(balanceOf[_from] >= _value);
        // 确保转移为正数个
        require(balanceOf[_to] + _value > balanceOf[_to]);
 
        // 以下用来检查交易
        uint previousBalances = balanceOf[_from] + balanceOf[_to];
        // 发送者账户余额减少
        balanceOf[_from] -= _value;
        // 接受者账户增加余额
        balanceOf[_to] += _value;
        Transfer(_from, _to, _value);
 
        // 用assert来检查代码逻辑。
        assert(balanceOf[_from] + balanceOf[_to] == previousBalances);
    }
 

    // Fix for short address attack against ERC20，避免短地址攻击
    modifier onlyPayloadSize(uint size) {
        assert(msg.data.length == size + 4);
        _;
    } 

    /**
     *  加密数字黄金交易公开接口
     * @param _to 接收者地址
     * @param _value 转移数额
     */
    function transfer(address _to, uint256 _value) public {
        _transfer(msg.sender, _to, _value);
    }
 
    /**
     * 账号之间加密数字黄金交易公开接口
     * @param _from 发送者地址
     * @param _to 接收者地址
     * @param _value 转移数额
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(_value <= allowance[_from][msg.sender]);     // Check allowance
        allowance[_from][msg.sender] -= _value;
        _transfer(_from, _to, _value);
        return true;
    }
 
    /**
     * 设置某个地址能从合约调用账户中转出数量为_value的黄金
     * 允许用户可花费的黄金
     * 调用方授权给定的地址可以从其地址中提款
     * 允许_spender多次转出黄金，最高达_value金额
     * @param _spender The address authorized to spend
     * @param _value the max amount they can spend
     */
    function approve(address _spender, uint256 _value) public
    returns (bool success) {
        allowance[msg.sender][_spender] = _value;
        return true;
    }
 
    /**
     * 设置允许一个地址（合约）以我（创建交易者）的名义可最多花费的黄金。
     * @param _spender 被授权的地址（合约）
     * @param _value 最大可花费加密数字黄金数
     * @param _extraData 发送给合约的附加数据
     */
    function approveAndCall(address _spender, uint256 _value, bytes _extraData)
    public
    returns (bool success) {
        tokenRecipient spender = tokenRecipient(_spender);
        if (approve(_spender, _value)) {
            // 通知合约
            spender.receiveApproval(msg.sender, _value, this, _extraData);
            return true;
        }
    }
 
    /**
     * 销毁我（创建交易者）账户中指定个加密数字黄金
     *-非ERC20标准
     */
    function burn(uint256 _value) public returns (bool success) {
        require(balanceOf[msg.sender] >= _value);   // 检查账户余额是否足够
        require(_value > 0); // 判断是否合法输入
        balanceOf[msg.sender] -= _value;            // 余额减去燃烧的数量
        totalSupply -= _value;                      // 总量也减少
        Burn(msg.sender, _value);
        return true;
    }
 
    /**
     * 销毁用户账户中指定个加密数字黄金
     *-非ERC20标准
     * @param _from the address of the sender
     * @param _value the amount of money to burn
     */
    function burnFrom(address _from, uint256 _value) public returns (bool success) {
        require(balanceOf[_from] >= _value);                // 检查账户余额是否足够
        require(_value <= allowance[_from][msg.sender]);    // Check allowance
        balanceOf[_from] -= _value;                         // 余额减去燃烧的数量
        allowance[_from][msg.sender] -= _value;             // Subtract from the sender's allowance
        totalSupply -= _value;                              // 总量也减少
        Burn(_from, _value);                                // 发送事件给前端
        return true;
    }


    // 可管理：冻结和解冻
    // 初始情况下用于流通的黄金会处于冻结状态，真正有挖掘流量时才会解冻对应的黄金数量
    function freeze(uint256 _value) public returns (bool success) {
        require(balanceOf[msg.sender] >= _value);            // 检查余额是否足够
        require(_value > 0); 
        balanceOf[msg.sender] -= _value;                      // 更新总数，从发送者中减去相应数量
        freezeOf[msg.sender] += _value;                       
        Freeze(msg.sender, _value);
        return true;
    }
 
    function unfreeze(uint256 _value) public returns (bool success) {
        require(freezeOf[msg.sender] >= _value);            // Check if the sender has enough
        require(_value > 0); 
        freezeOf[msg.sender] -= _value;                      // 从发送者中减去相应数量
        balanceOf[msg.sender] += _value;                     // 更新总数
        Unfreeze(msg.sender, _value);
        return true;
    }
}
