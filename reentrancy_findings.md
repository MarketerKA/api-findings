# Security Findings Report

**Search Query:** `reentrancy`

**Total Found:** 226 findings

**Exported:** 20 findings

**Generated:** 2026-02-04 04:22:25

## Statistics

**Average Quality:** 2.00/5

- **HIGH:** 20 (100.0%)

---

## Table of Contents

1. [HIGH] [[H-13] Possible reentrancy and fund theft in `withdrawDETH()` of `GiantSavETHVaultPool` because there is no whitelist check for user provided Vaults and there is no reentrancy defense](#finding-1)
2. [HIGH] [[H-13] Possible reentrancy and fund theft in withdrawDETH() of GiantSavETHVaultPool because there is no whitelist check for user provided Vaults and there is no reentrancy defense](#finding-2)
3. [HIGH] [H-1: Cross-contract reentrancy allows YIELD_TOKEN theft for the `GenericERC4626` `WithdrawalRequestManager` variant](#finding-3)
4. [HIGH] [Read-only reentrancy](#finding-4)
5. [HIGH] [`redeemNative()` Reentrancy Enables Permanent Fund Freeze, Systemic Misaccounting, and Liquidation Cascades](#finding-5)
6. [HIGH] [H-3: Reentrancy in Vesting.sol:claim() will allow users to drain the contract due to executing .call() on user's address before setting s.index = uint128(i)](#finding-6)
7. [HIGH] [H-3: Signers can bypass checks to add new modules to a safe by abusing reentrancy](#finding-7)
8. [HIGH] [H-7: Signers can bypass checks to add new modules to a safe by abusing reentrancy](#finding-8)
9. [HIGH] [[H-20] Possibly reentrancy attacks in `_distributeETHRewardsToUserForToken` function](#finding-9)
10. [HIGH] [[H-20] Possibly reentrancy attacks in _distributeETHRewardsToUserForToken function](#finding-10)
11. [HIGH] [Reentrancy Guard Conflict in `_processVaultRewards` Private Function](#finding-11)
12. [HIGH] [[H-18] Reentrancy attack possible on `RootBridgeAgent.retrySettlement()` with missing access control for `RootBridgeAgentFactory.createBridgeAgent()`](#finding-12)
13. [HIGH] [[H-05] Reentrancy in LiquidStakingManager.sol#withdrawETHForKnow leads to loss of fund from smart wallet](#finding-13)
14. [HIGH] [Reentrancy in `EscrowManager`](#finding-14)
15. [HIGH] [Malicious User Can Drain Rewards Through Reentrancy in Staking](#finding-15)
16. [HIGH] [Reentrancy attack to duplicate NFT tier to other contracts ](#finding-16)
17. [HIGH] [Reentrancy in StEthHyperdrive.openShort](#finding-17)
18. [HIGH] [RocketNodeDistributorDelegate - Reentrancy in distribute() allows node owner to drain distributor funds ✓ Fixed](#finding-18)
19. [HIGH] [[H-05] Reentrancy in `LiquidStakingManager.sol#withdrawETHForKnow` leads to loss of fund from smart wallet](#finding-19)
20. [HIGH] [Reentrancy Vulnerability Allows Draining All Funds](#finding-20)

---

## Finding #1: [H-13] Possible reentrancy and fund theft in `withdrawDETH()` of `GiantSavETHVaultPool` because there is no whitelist check for user provided Vaults and there is no reentrancy defense {#finding-1}

| Property | Value |
|----------|-------|
| **Impact** | HIGH |
| **Quality** | 0/5 |
| **Firm** | Code4rena |
| **Protocol** | Stakehouse Protocol |
| **Links** | [Source](https://code4rena.com/reports/2022-11-stakehouse) · [GitHub](https://github.com/code-423n4/2022-11-stakehouse-findings/issues/226) |

**Found by:** unforgiven

---

Function `withdrawDETH()` in `GiantSavETHVaultPool` allows a user to burn their giant LP in exchange for dETH that is ready to withdraw from a set of savETH vaults. This function make external calls to user provided addresses without checking those addresses and send increased dETH balance of contract during the call to user. User can provide malicious addresses to contract and then took the execution flow during the transaction and increase dETH balance of contract by other calls and make contract to transfer them to him.

#
### Tools Used

VIM

### Recommended Mitigation Steps

Check the provided addresses and also have some reentrancy defense mechanisim.

**[vince0656 (Stakehouse) confirmed](https://github.com/code-423n4/2022-11-stakehouse-findings/issues/226)**

***

---

## Finding #2: [H-13] Possible reentrancy and fund theft in withdrawDETH() of GiantSavETHVaultPool because there is no whitelist check for user provided Vaults and there is no reentrancy defense {#finding-2}

| Property | Value |
|----------|-------|
| **Impact** | HIGH |
| **Quality** | 3.6666666666666665/5 |
| **Firm** | Code4rena |
| **Protocol** | Stakehouse Protocol |
| **Links** | [Source](https://code4rena.com/reports/2022-11-stakehouse) · [GitHub](https://github.com/code-423n4/2022-11-stakehouse-findings/issues/226) |

**Tags:** `Reentrancy`

**Found by:** unforgiven

---

## Lines of code

https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantSavETHVaultPool.sol#L62-L102

## Vulnerability details

## Impact
Function `withdrawDETH()` in `GiantSavETHVaultPool` allows a user to burn their giant LP in exchange for dETH that is ready to withdraw from a set of savETH vaults. This function make external calls to user provided addresses without checking those addresses and send increased dETH balance of contract during the call to user. user can provide malicious addresses to contract and then took the execution flow during the transaction and increase dETH balance of contract by other calls and make contract to transfer them to him.

## Tools Used
VIM

## Recommended Mitigation Steps
check the provided addresses and also have some reentrancy defence mechanisim.

---

## Finding #3: H-1: Cross-contract reentrancy allows YIELD_TOKEN theft for the `GenericERC4626` `WithdrawalRequestManager` variant {#finding-3}

| Property | Value |
|----------|-------|
| **Impact** | HIGH |
| **Quality** | 0/5 |
| **Firm** | Sherlock |
| **Protocol** | Notional Exponent |
| **Links** | [GitHub](https://github.com/sherlock-audit/2025-06-notional-exponent-judging/issues/73) |

**Found by:** talfao, KungFuPa, 0xBoraichoT, Ragnarok

---

Source: https://github.com/sherlock-audit/2025-06-notional-exponent-judging/issues/73 

## Found by 
0xBoraichoT, KungFuPanda, Ragnarok, talfao

- https://github.com/notional-finance/leveraged-vaults/blob/7e0abc3e118db0abb20c7521c6f53f1762fdf562/contracts/trading/adapters/UniV3Adapter.sol#L60-L72

^ The only validations in-place are the tokenIn and tokenOut sanitizations, but not the whole multihop path though.

<img width="815" height="481" alt="Image" src="https://sherlock-files.ams3.digitaloceanspaces.com/gh-images/b8f9b6b7-8401-4160-aa5a-c678f49bb7f7" />

_NOTE_ This is the Trading module we have: https://etherscan.io/address/0x179a2d2408bfbc21b72d59c4a74e5010f07dc823#code

![Image](https://sherlock-files.ams3.digitaloceanspaces.com/gh-images/b2d7e6ee-c3ab-44b9-bb85-1986f4418d07)

https://etherscan.io/address/0xE592427A0AEce92De3Edee1F18E0157C05861564#code <-- UniswapV3 router

## Description
Since the `WithdrawalRequestManager` allows `onlyVault` operations for multiple different strategy "vaults",..

A combination of a default reentrancy + cross-contract reentrancy is possible...

...Through which `YIELD_TOKEN`s can be drained from the `WithdrawalRequestManager`...

...---> to the yield strategy where the strategy's `depositAsset != WithdrawalRequestManager.STAKE_TOKEN`.

This way, the strategy will record a higher surplus (aka delta) of `YIELD_TOKEN`s in the current `YIELD_TOKEN.balanceOf(address(this))` and will mint more shares to the malicious user's account.

`onlyApprovedVault` permits any caller whitelisted in the `isApprovedVault` mapping:
```solidity
    /// @dev Ensures that only approved vaults can initiate withdraw requests.
    modifier onlyApprovedVault() {
        if (!isApprovedVault[msg.sender]) revert Unauthorized(msg.sender);
        _;
    }
```

Thus, it is possible to steal funds from the `WithdrawalRequestManager` and then burn these `YIELD_TOKEN`s in exchange for deposit underlying staking token assets.

## Root cause
A single `WithdrawalRequestManager` permits multiple `AbstractYieldStrategy` instances (aka "whitelisted vaults").

Since neither the `WithdrawalRequestManager.stakeTokens` nor `WithdrawalRequestManager.initiateWithdraw` functions have a `nonReentrant` modifier or an equivalent cross-contract reentrancy protection method, the 

```solidity
    function _initiateWithdraw(
        address account,
        uint256 yieldTokenAmount,
        uint256 sharesHeld,
        bytes memory data
    ) internal override virtual returns (uint256 requestId) {
        ERC20(yieldToken).approve(address(withdrawRequestManager), yieldTokenAmount);
        requestId = withdrawRequestManager.initiateWithdraw({ // audit: reentrancy here!!!!
            account: account, yieldTokenAmount: yieldTokenAmount, sharesAmount: sharesHeld, data: data
        });
    } // audit: does this affect the yield token balance somehow?

    /// @dev By default we can use the withdraw request manager to stake the tokens
    function _mintYieldTokens(uint256 assets, address /* receiver */, bytes memory depositData) internal override virtual { // audit: can it be reentered to increase the yieldtoken balance somehow???
        ERC20(asset).approve(address(withdrawRequestManager), assets); // audit: reverts for USDT
        withdrawRequestManager.stakeTokens(address(asset), assets, depositData); // audit malicious data
    }
```

*[Long code block removed]*

```solidity
/ @dev Used for ERC4626s that can be staked and unstaked on demand without any additional
/// time constraints.
contract GenericERC4626WithdrawRequestManager is AbstractWithdrawRequestManager {

    uint256 private currentRequestId;
    mapping(uint256 => uint256) private s_withdrawRequestShares;

    constructor(address _erc4626)
        AbstractWithdrawRequestManager(IERC4626(_erc4626).asset(), _erc4626, IERC4626(_erc4626).asset()) { }

    function _initiateWithdrawImpl(
        address /* account */,
        uint256 sharesToWithdraw,
        bytes calldata /* data */
    ) override internal returns (uint256 requestId) {
        requestId = ++currentRequestId;
        s_withdrawRequestShares[requestId] = sharesToWithdraw;
    }

    function _stakeTokens(uint256 amount, bytes memory /* stakeData */) internal override {
        ERC20(STAKING_TOKEN).approve(address(YIELD_TOKEN), amount);
        IERC4626(YIELD_TOKEN).deposit(amount, address(this));
    }

    function _finalizeWithdrawImpl(
        address /* account */,
        uint256 requestId
    ) internal override returns (uint256 tokensClaimed, bool finalized) {
        uint256 sharesToRedeem = s_withdrawRequestShares[requestId];
        delete s_withdrawRequestShares[requestId];
        tokensClaimed = IERC4626(YIELD_TOKEN).redeem(sharesToRedeem, address(this), address(this));
        finalized = true;
        // audit: increases the yieldtoken balance
    }

    function canFinalizeWithdrawRequest(uint256 /* requestId */) public pure override returns (bool) {
        return true;
    }
}
```

## Attack path

When the `WithdrawalRequestManager` is using the `GenericERC4626` functionality variant:..

```solidity
/ @dev Used for ERC4626s that can be staked and unstaked on demand without any additional
/// time constraints.
contract GenericERC4626WithdrawRequestManager is AbstractWithdrawRequestManager {

    uint256 private currentRequestId;
    mapping(uint256 => uint256) private s_withdrawRequestShares;

    constructor(address _erc4626)
        AbstractWithdrawRequestManager(IERC4626(_erc4626).asset(), _erc4626, IERC4626(_erc4626).asset()) { }

    function _initiateWithdrawImpl(
        address /* account */,
        uint256 sharesToWithdraw,
        bytes calldata /* data */
    ) override internal returns (uint256 requestId) {
        requestId = ++currentRequestId;
        s_withdrawRequestShares[requestId] = sharesToWithdraw;
    }

    function _stakeTokens(uint256 amount, bytes memory /* stakeData */) internal override {
        ERC20(STAKING_TOKEN).approve(address(YIELD_TOKEN), amount);
        IERC4626(YIELD_TOKEN).deposit(amount, address(this));
    }

    function _finalizeWithdrawImpl(
        address /* account */,
        uint256 requestId
    ) internal override returns (uint256 tokensClaimed, bool finalized) {
        uint256 sharesToRedeem = s_withdrawRequestShares[requestId];
        delete s_withdrawRequestShares[requestId];
        tokensClaimed = IERC4626(YIELD_TOKEN).redeem(sharesToRedeem, address(this), address(this));
        finalized = true;
        // audit: increases the yieldtoken balance
    }

    function canFinalizeWithdrawRequest(uint256 /* requestId */) public pure override returns (bool) {
        return true;
    }
}
```

... The users who request redemptions (via `initiateWithdraw`) just temporarily leave sparse `YIELD_TOKEN`s in the `WithdrawalRequestManager`.

**It is a crucial observation needed for proving the validity of the suggested cross-contract reentrancy attack.**

## External preconditions
**Spare `YIELD_TOKEN`s in the `WithdrawalRequestManager`'s `GenericERC4626` variant as a result of other users calling `initateWithdraw` and leaving pending redemption requests.**

_NOTE_ **Either through front-running or just proper timing, the attack will be executed before the requester calls `finalizeAndRedeemWithdrawRequest` or `finalizeRequestManual` is called.**

1.

*[Long code block removed]*

2. 
```solidity
     function mintShares(
        uint256 assetAmount,
        address receiver,
        bytes calldata depositData
    ) external override onlyLendingRouter setCurrentAccount(receiver) nonReentrant returns (uint256 sharesMinted) {
        // Cannot mint shares if the receiver has an active withdraw request
        if (_isWithdrawRequestPending(receiver)) revert CannotEnterPosition();
        ERC20(asset).safeTransferFrom(t_CurrentLendingRouter, address(this), assetAmount);
        sharesMinted = _mintSharesGivenAssets(assetAmount, depositData, receiver); // audit: unsanitized depositData

        t_AllowTransfer_To = t_CurrentLendingRouter;
        t_AllowTransfer_Amount = sharesMinted;
        // Transfer the shares to the lending router so it can supply collateral
        _transfer(receiver, t_CurrentLendingRouter, sharesMinted);
    }

    /// @dev Marked as virtual to allow for RewardManagerMixin to override
    function _mintSharesGivenAssets(uint256 assets, bytes memory depositData, address receiver) internal virtual returns (uint256 sharesMinted) { // audit
        if (assets == 0) return 0;

        // First accrue fees on the yield token
        _accrueFees();
        uint256 initialYieldTokenBalance = _yieldTokenBalance();
        _mintYieldTokens(assets, receiver, depositData); // audit
        uint256 yieldTokensMinted = _yieldTokenBalance() - initialYieldTokenBalance; // audit: can this be manipulated through reentrancy somehow???

        sharesMinted = (yieldTokensMinted * effectiveSupply()) / (initialYieldTokenBalance - feesAccrued() + VIRTUAL_YIELD_TOKENS); // audit: effectiveSupply can be manipulated to become greater than intended
        _mint(receiver, sharesMinted); // audit: reentrant
    }
```
3.
```solidity
     /// @dev By default we can use the withdraw request manager to stake the tokens
    function _mintYieldTokens(uint256 assets, address /* receiver */, bytes memory depositData) internal override virtual { // audit: can it be reentered to increase the yieldtoken balance somehow???
        ERC20(asset).approve(address(withdrawRequestManager), assets); // audit: reverts for USDT
        withdrawRequestManager.stakeTokens(address(asset), assets, depositData); // audit malicious data
    }
```
4.
```solidity
    function _initiateWithdraw(
        address account,
        uint256 yieldTokenAmount,
        uint256 sharesHeld,
        bytes memory data
    ) internal override virtual returns (uint256 requestId) {
        ERC20(yieldToken).approve(address(withdrawRequestManager), yieldTokenAmount);
        requestId = withdrawRequestManager.initiateWithdraw({ // audit: reentrancy here!!!!
            account: account, yieldTokenAmount: yieldTokenAmount, sharesAmount: sharesHeld, data: data
        });
    } // audit: does this affect the yield token balance somehow?
```

_NOTE_ The Uniswap multihop trade data should include a malicious swap middle pool to make the reentrancy callback itself even possible.

You can see the e2e PoC at the end of this report.

## Internal preconditions
None.

## Impact
Theft of other users' funds via stealing `YIELD_TOKEN`s from the pending ERC4626-variant `WithdrawalRequestManager` requests of other users.
```solidity
    /// @inheritdoc IYieldStrategy
    function initiateWithdraw(
        address account,
        uint256 sharesHeld,
        bytes calldata data
    ) external onlyLendingRouter setCurrentAccount(account) override returns (uint256 requestId) {
        requestId = _withdraw(account, sharesHeld, data); // audit: lacks nonreentrant modifier
    }

    /// @inheritdoc IYieldStrategy
    /// @dev We do not set the current account here because valuation is not done in this method. A
    /// native balance does not require a collateral check.
    function initiateWithdrawNative(
        bytes memory data // audit: lscks nonReentrant, so can reenter exactly here
    ) external override returns (uint256 requestId) { // audit: lacks the nonReentrant modifier
        requestId = _withdraw(msg.sender, balanceOf(msg.sender), data); // audit: unsanitized data
    }

    function _withdraw(address account, uint256 sharesHeld, bytes memory data) internal returns (uint256 requestId) {
        if (sharesHeld == 0) revert InsufficientSharesHeld();

        // Accrue fees before initiating a withdraw since it will change the effective supply
        _accrueFees();
        uint256 yieldTokenAmount = convertSharesToYieldToken(sharesHeld);
        requestId = _initiateWithdraw(account, yieldTokenAmount, sharesHeld, data);
        // Escrow the shares after the withdraw since it will change the effective supply
        // during reward claims when using the RewardManagerMixin.
        s_escrowedShares += sharesHeld;

    }
```

*[Long code block removed]*

The only swap path validations are ensuring the first and last tokens match expected values (tokenIn and deUSD in correct order) and a minimum length. This allows an attacker to insert their own malicious token and pool addresses mid-path. During the Uniswap swap, when execution reaches the attacker-controlled pool, the attacker’s token contract can execute arbitrary code in its transfer function. By coding this hook to reenter the Jigsaw protocol—specifically, calling HoldingManager.deposit—the attacker can deposit some new tokens before the swap completes.

```solidity
    function _exactInBatch(address from, Trade memory trade) private pure returns (bytes memory) {
        UniV3BatchData memory data = abi.decode(trade.exchangeData, (UniV3BatchData));

        // Validate path EXACT_IN = [sellToken, fee, ... buyToken]
        require(32 <= data.path.length);
        require(_toAddress(data.path, 0) == _getTokenAddress(trade.sellToken));
        require(_toAddress(data.path, data.path.length - 20) == _getTokenAddress(trade.buyToken));

        ISwapRouter.ExactInputParams memory params = ISwapRouter.ExactInputParams(
            data.path, from, trade.deadline, trade.amount, trade.limit
        );

        return abi.encodeWithSelector(ISwapRouter.exactInput.selector, params);
    }
```

```solidity
    function _getExecutionData(
        uint16 dexId,
        address from,
        Trade memory trade
    )
        internal
        pure
        returns (
            address spender,
            address target,
            uint256 msgValue,
            bytes memory executionCallData
        )
    {
        if (trade.buyToken == trade.sellToken) revert SellTokenEqualsBuyToken();

        if (DexId(dexId) == DexId.UNISWAP_V3) {
            return UniV3Adapter.getExecutionData(from, trade);
        } else if (DexId(dexId) == DexId.BALANCER_V2) {
```

```solidity

    /// @dev Initiates a withdraw request for the vault shares held by the account
    function _initiateWithdraw(
        address vault,
        address account,
        bytes calldata data
    ) internal returns (uint256 requestId) {
        uint256 sharesHeld = balanceOfCollateral(account, vault);
        if (sharesHeld == 0) revert InsufficientSharesHeld();
        return IYieldStrategy(vault).initiateWithdraw(account, sharesHeld, data); // audit
    }
```

https://gist.github.com/c-plus-plus-equals-c-plus-one/500a3df82f34eb894db54a4e619fcfed

## Mitigation
The "before balance" state accounting hould be captured **after** the `_preStakingTrade` call:
```diff
    /// @inheritdoc IWithdrawRequestManager
    function stakeTokens(
        address depositToken,
        uint256 amount,
        bytes calldata data // audit
    ) external override onlyApprovedVault returns (uint256 yieldTokensMinted) { // @audit: should actually be non reentrant I think
-       uint256 initialYieldTokenBalance = ERC20(YIELD_TOKEN).balanceOf(address(this));
        ERC20(depositToken).safeTransferFrom(msg.sender, address(this), amount);
        (uint256 stakeTokenAmount, bytes memory stakeData) = _preStakingTrade(depositToken, amount, data); // audit: reenter and call initiateWithdraw from a diffferent vault (i.e., cross-contract reentrancy)
+       uint256 initialYieldTokenBalance = ERC20(YIELD_TOKEN).balanceOf(address(this));
        _stakeTokens(stakeTokenAmount, stakeData);

        yieldTokensMinted = ERC20(YIELD_TOKEN).balanceOf(address(this)) - initialYieldTokenBalance; // audit: REENTRANCY HERE??? 🪻🪻🪻
        ERC20(YIELD_TOKEN).safeTransfer(msg.sender, yieldTokensMinted);
    }
    
```

---

## Finding #4: Read-only reentrancy {#finding-4}

| Property | Value |
|----------|-------|
| **Impact** | HIGH |
| **Quality** | 5/5 |
| **Firm** | Cyfrin |
| **Protocol** | Beanstalk Wells |
| **Links** | [Source](https://github.com/solodit/solodit_content/blob/main/reports/Cyfrin/2023-06-16-Beanstalk wells.md) |

**Tags:** `Read-only Reentrancy`

**Found by:** Hans, Alex Roan, Patrick Collins, Giovanni Di Siena

---

**Description:** The current implementation is vulnerable to read-only reentrancy, especially in [Wells::removeLiquidity](https://github.com/BeanstalkFarms/Wells/blob/e5441fc78f0fd4b77a898812d0fd22cb43a0af55/src/Well.sol#L440).
The implementation does not strictly follow the [Checks-Effects-Interactions (CEI) pattern](https://fravoll.github.io/solidity-patterns/checks_effects_interactions.html) as it is setting the new reserve values after sending out the tokens. This is not an immediate risk to the protocol itself due to the `nonReentrant` modifier, but this is still vulnerable to [read-only reentrancy](https://chainsecurity.com/curve-lp-oracle-manipulation-post-mortem/).

Malicious attackers and unsuspecting ecosystem participants can deploy Wells with ERC-777 tokens (which have a callback that can take control) and exploit this vulnerability. This will lead to critical vulnerabilities given that the Wells are to be extended with price functions as defined by pumps - third-party protocols that integrate these on-chain oracles will be at risk.

Pumps are updated before token transfers; however, reserves are only set after. Therefore, pump functions will likely be incorrect on a re-entrant read-only call if `IWell(well).getReserves()` is called but reserves have not been correctly updated. The implementation of `GeoEmaAndCumSmaPump` appears not to be vulnerable, but given that each pump can choose its approach for recording a well's reserves over time, this remains a possible attack vector.

**Impact:** Although this is not an immediate risk to the protocol itself, read-only re-entrancy can lead to critical issues, so we evaluate the severity as HIGH.

**Recommended Mitigation:** Implement the CEI pattern in relevant functions by updating reserves before making external calls. For example, the function `Well::removeLiquidity` can be modified shown below.

```solidity
function removeLiquidity(
    uint lpAmountIn,
    uint[] calldata minTokenAmountsOut,
    address recipient
) external nonReentrant returns (uint[] memory tokenAmountsOut) {
    IERC20[] memory _tokens = tokens();
    uint[] memory reserves = _updatePumps(_tokens.length);
    uint lpTokenSupply = totalSupply();

    tokenAmountsOut = new uint[](_tokens.length);
    _burn(msg.sender, lpAmountIn);

    _setReserves(reserves); // @audit CEI pattern

    for (uint i; i < _tokens.length; ++i) {
        tokenAmountsOut[i] = (lpAmountIn * reserves[i]) / lpTokenSupply;
        require(
            tokenAmountsOut[i] >= minTokenAmountsOut[i],
            "Well: slippage"
        );
        _tokens[i].safeTransfer(recipient, tokenAmountsOut[i]);
        reserves[i] = reserves[i] - tokenAmountsOut[i];
    }

    emit RemoveLiquidity(lpAmountIn, tokenAmountsOut);
}
```

**Beanstalk:** Added a check to the `getReserves()` function that reverts if the Reentrancy guard has been entered. This prevents anyone from calling `getReserves()` while executing a function in the Well. Fixed in commit [fcbf04a](https://github.com/BeanstalkFarms/Basin/pull/85/commits/fcbf04a99b00807891fb2a9791ba18ed425479ab).

**Cyfrin:** Acknowledged.

\clearpage

---

## Finding #5: `redeemNative()` Reentrancy Enables Permanent Fund Freeze, Systemic Misaccounting, and Liquidation Cascades {#finding-5}

| Property | Value |
|----------|-------|
| **Impact** | HIGH |
| **Quality** | 5/5 |
| **Firm** | MixBytes |
| **Protocol** | Notional Finance |
| **Links** | [Source](https://github.com/mixbytes/audits_public/blob/master/Notional%20Finance/Notional%20v4/README.md#1-redeemnative-reentrancy-enables-permanent-fund-freeze-systemic-misaccounting-and-liquidation-cascades) |

**Found by:** MixBytes

---

##### Description
The redemption flow in `AbstractYieldStrategy.redeemNative()` is vulnerable to reentrancy that corrupts internal accounting and can permanently freeze a portion of the vault's yield tokens. The `redeemNative()` function calls `AbstractStakingStrategy._redeemShares()`, which for instant redemption delegates to `AbstractYieldStrategy._executeTrade()` and performs an external call during redemption. Not all vault and router entry points are protected against reentrancy, which allows control to reenter from the lending router while `_burnShares()` is still executing. A malicious token placed on the swap path can exploit this by reentering and invoking `ILendingRouter.initiateWithdraw()` during the redemption.

When reentrancy occurs, the request manager transfers an amount N of yield tokens from the vault. This decreases the vault's true yield token balance along with `s_yieldTokenBalance` while `_burnShares()` continues to run based on a pre‑reentrancy snapshot. After control returns, `_burnShares()` computes `yieldTokensRedeemed = yieldTokensBefore - yieldTokensAfter` and then subtracts this value from `s_yieldTokenBalance`. Since `yieldTokensBefore` was taken before the reentrancy and the request manager already moved N tokens, `s_yieldTokenBalance` is effectively reduced twice for N. The resulting difference causes yield tokens to become unaccounted by internal state and remain frozen in the vault. This also distorts share pricing and may reduce health factors enough to trigger liquidations, enabling repeated exploitation, potentially leading to full vault fund freezing.

It is also possible to trigger a similar reentrancy through `AbstractYieldStrategy.collectFees()`, since it reduces the vault's yield token balance and `s_yieldTokenBalance`. The impact is smaller because fee collection typically moves a limited amount of tokens, but the accounting discrepancy mechanism is analogous.

**Attack Path:**

1. The attacker deploys a malicious ERC20 token and creates Uniswap V2 pools to form a swap path `yieldToken -> maliciousToken -> asset`.
2. The attacker enters a position via the lending router and gives approval to the malicious token to perform `initiateWithdraw` later on it.
3. The attacker ensures they hold native shares without an open position by liquidating another account first, following the protocol’s constraints.
4. The attacker calls `redeemNative` using the instant redemption path and sets `exchangeData` to the Uniswap V2 path that includes the malicious token.
5. During the Uniswap V2 swap, the malicious token’s `transfer()` reenters and calls `ILendingRouter.initiateWithdraw(attacker, vault, ...)` while `_burnShares()` is still running.
6. The Withdraw Request Manager transfers N yield tokens from the vault during reentrancy, decreasing the vault’s true yield token balance with `s_yieldTokenBalance` aswell.
7. Control returns to `_burnShares()`, which computes `yieldTokensRedeemed` using the pre‑reentrancy snapshot and subtracts it from `s_yieldTokenBalance`. The result is an effective subtraction of M + 2N, leaving N yield tokens unaccounted by internal state and thus frozen.
8. The mismatch between `ERC20(yieldToken).balanceOf(address(y))` and `s_yieldTokenBalance` becomes observable. Health factors can drop, triggering liquidations and enabling repeated exploitation.

Here is the proof of concept that shows the attack:

Firstly, put these lines into `MockStakingStrategy` contract:

```solidity
// Expose internal state for testing
function _s_yieldTokenBalance() external view returns (uint256) {
    return s_yieldTokenBalance;
}
```

Then, put this file into `tests` folder and run it with `forge test --match-test test_reentrancy_redeemNative_initiateWithdraw_instant -vvv`:

*[Long code block removed]*

The results of the test are as follows:

```
Before liquidation - s_yieldTokenBalance: 14414159849677474491
Before liquidation - yield token balance: 14414159849677474491
Before liquidation - share total supply: 14414159849677474491000000
Before liquidation - share price attacker: 1071991787524217088000000000000
Before liquidation - share price user2: 1071991787524217088000000000000
Before liquidation - collateralValue: 9968942569622939455
Before liquidation - maxBorrow: 9121582451204989601
After liquidation - s_yieldTokenBalance: 107408739525016019612
After liquidation - yield token balance: 107408739525016019612
After liquidation - share total supply: 107408739525016019612000000
After liquidation - share price attacker: 1071991775286867985000000000000
After liquidation - share price user2: 1071991775286867985000000000000
After liquidation - collateralValue: 9968942455822225838
After liquidation - maxBorrow: 9121582347077336641
Shares balance of attacker 5114701882143619980000000
Shares balance of liquidator 92994579675338545121000000
After attack - s_yieldTokenBalance: 4184757263746203114
After attack - yield token balance: 9299459087502815641
After attack - share total supply: 14414159849677474491000000
After attack - share price attacker: 1071991775286867985000000000000
After attack - share price user2: 482396298879090593000000000000
After attack - collateralValue: 4486024105120001625
After attack - maxBorrow: 4104712056184801486
```

We see that `s_yieldTokenBalance` is twice less than yield token balance after attack, and `collateralValue` and `maxBorrow` of attacked position holder is decreased more than 2 times, though they didn't change their position themselves.

This issue is classified as **Critical** severity because it allows a malicious actor to corrupt accounting, freeze user funds inside the vault, distort share pricing, and potentially cause cascading liquidations leading to systemic protocol failure.

##### Recommendation
We recommend making the following changes:
1. Add a `nonReentrant` guard to all external entry points that can be reached during redemption and accounting updates, including lending router functions, and functions in request manager such as `initiateWithdraw()` and `finalize()`. We would also suggest to add guard to as much external functions of the protocol as possible, to eliminate attack possibility totally.
2. Validate `exchangeData` for Uniswap V2 trades and enforce that the path contains exactly **two tokens** (single-hop swap) to prevent insertion of arbitrary intermediary tokens that can perform reentrancy during transfer.

> **Client's Commentary:** 
> Fixed here: https://github.com/notional-finance/notional-v4/pull/34/commits/abcd6bef62b2c53cc8f680b92c8554a1a0474c4e

---

---

## Finding #6: H-3: Reentrancy in Vesting.sol:claim() will allow users to drain the contract due to executing .call() on user's address before setting s.index = uint128(i) {#finding-6}

| Property | Value |
|----------|-------|
| **Impact** | HIGH |
| **Quality** | 2/5 |
| **Firm** | Sherlock |
| **Protocol** | Zap Protocol |
| **Links** | [GitHub](https://github.com/sherlock-audit/2024-03-zap-protocol-judging/issues/157) |

**Tags:** `Reentrancy`

**Found by:** ZdravkoHr., klaus, no, cats, cawfree, novaman33, psb01, Silvermist, aman, mike-watson, denzi\_, 0xR360, AMOW, BengalCatBalu, 404666, nilay27, 0x4non, turvec, Varun\_05, bughuntoor, thank\_you, 0xhashiman, s1ce, UbiquitousComputing, enfrasico, dipp, HonorLt

---

Source: https://github.com/sherlock-audit/2024-03-zap-protocol-judging/issues/157 

## Found by 
0x4non, 0xR360, 0xhashiman, 404666, AMOW, BengalCatBalu, HonorLt, Silvermist, UbiquitousComputing, Varun\_05, ZdravkoHr., aman, bughuntoor, cats, cawfree, denzi\_, dipp, enfrasico, klaus, mike-watson, nilay27, no, novaman33, psb01, s1ce, thank\_you, turvec

## Vulnerability Detail
Here is the Vesting.sol:claim() function:
```solidity
function claim() external {
        address sender = msg.sender;

        UserDetails storage s = userdetails[sender];
        require(s.userDeposit != 0, "No Deposit");
@>      require(s.index != vestingPoints.length, "already claimed");
        uint256 pctAmount;
        uint256 i = s.index;
        for (i; i <= vestingPoints.length - 1; i++) {
            if (block.timestamp >= vestingPoints[i][0]) {
                pctAmount += (s.userDeposit * vestingPoints[i][1]) / 10000;
            } else {
                break;
            }
        }
        if (pctAmount != 0) {
            if (address(token) == address(1)) {
@>              (bool sent, ) = payable(sender).call{value: pctAmount}("");
                require(sent, "Failed to send BNB to receiver");
            } else {
                token.safeTransfer(sender, pctAmount);
            }
@>          s.index = uint128(i);
            s.amountClaimed += pctAmount;
        }
    }
```
From the above, You'll notice the claim() function checks if the caller already claimed by checking if the s.index has already been set to vestingPoints.length. You'll also notice the claim() function executes .call() and transfer the amount to the caller before setting the s.index = uint128(i), thereby allowing reentrancy.

Let's consider this sample scenario:
- An attacker contract(alice) has some native pctAmount to claim and calls `claim()`.
- "already claimed" check will pass since it's the first time she's calling `claim()` so her s.index hasn't been set
- However before updating Alice s.index, the Vesting contract performs external .call() to Alice with the amount sent as well
- Alice reenters `claim()` again on receive of the amount
- bypass index "already claimed" check since this hasn't been updated yet
- contract performs external .call() to Alice with the amount sent as well again,
- Same thing happens again
- Alice ends up draining the Vesting contract

## Impact
Reentrancy in Vesting.sol:claim() will allow users to drain the contract

## Code Snippet
https://github.com/sherlock-audit/2024-03-zap-protocol/blob/main/zap-contracts-labs/contracts/Vesting.sol#L84
https://github.com/sherlock-audit/2024-03-zap-protocol/blob/main/zap-contracts-labs/contracts/Vesting.sol#L89

## Tool used

Manual Review

## Recommendation
Here is the recommended fix:
```diff
if (pctAmount != 0) {
+           s.index = uint128(i);
            if (address(token) == address(1)) {
                (bool sent, ) = payable(sender).call{value: pctAmount}("");
                require(sent, "Failed to send BNB to receiver");
            } else {
                token.safeTransfer(sender, pctAmount);
            }
-           s.index = uint128(i);
            s.amountClaimed += pctAmount;
        }
```
I'll also recommend using reentrancyGuard.

## Discussion

**midori-fuse**

Escalate 

Per Sherlock's [duplication rule](https://docs.sherlock.xyz/audits/judging/judging#ix.-duplication-rules):

> In the above example if the root issue A is one of the following generic vulnerabilities:
> - Reentrancy
> - Access control
> - Front-running
>
> Then the submissions with valid attack paths and higher vulnerability are considered valid. If the submission is vague or does not identify the attack path with higher severity clearly it will be considered low.
> - B is a valid issue
> - C is low

The following submissions fail to and/or incorrectly identify the root cause that enables the attack path: #6 #34 #66 #68 #79 #90 #98 #132 #149  . 
- The issues in this category should be Low.

The following submissions are somewhat vague, but did manage to identify the erroneous storage variable that leads to re-entrancy (`s.index`): #10 #53 #104 #138 #186 (and a few more). 
- While they did not (or vaguely) described the "attack path", the attack path here is just "directly calling `claim()` in your `receive()`", so I suppose one can be ok with just spelling out the function and the wrong storage variable.
- Since submission quality is subjective, I am flagging these issues so the judges can help with reviewing dupes. Personally I think these submissions are still acceptable, but leaving to the judges to decide the where the bar is.

**sherlock-admin2**

> Escalate 
> 
> Per Sherlock's [duplication rule](https://docs.sherlock.xyz/audits/judging/judging#ix.-duplication-rules):
> 
> > In the above example if the root issue A is one of the following generic vulnerabilities:
> > - Reentrancy
> > - Access control
> > - Front-running
> >
> > Then the submissions with valid attack paths and higher vulnerability are considered valid. If the submission is vague or does not identify the attack path with higher severity clearly it will be considered low.
> > - B is a valid issue
> > - C is low
> 
> The following submissions fail to and/or incorrectly identify the root cause that enables the attack path: #6 #34 #66 #68 #79 #90 #98 #132 #149  . 
> - The issues in this category should be Low.
> 
> The following submissions are somewhat vague, but did manage to identify the erroneous storage variable that leads to re-entrancy (`s.index`): #10 #53 #104 #138 #186 (and a few more). 
> - While they did not (or vaguely) described the "attack path", the attack path here is just "directly calling `claim()` in your `receive()`", so I suppose one can be ok with just spelling out the function and the wrong storage variable.
> - Since submission quality is subjective, I am flagging these issues so the judges can help with reviewing dupes. Personally I think these submissions are still acceptable, but leaving to the judges to decide the where the bar is.

You've created a valid escalation!

To remove the escalation from consideration: Delete your comment.

You may delete or edit your escalation comment anytime before the 48-hour escalation window closes. After that, the escalation becomes final.

**Nilay27**

> Escalate
> 
> Per Sherlock's [duplication rule](https://docs.sherlock.xyz/audits/judging/judging#ix.-duplication-rules):
> 
> > In the above example if the root issue A is one of the following generic vulnerabilities:
> > 
> > * Reentrancy
> > * Access control
> > * Front-running
> > 
> > Then the submissions with valid attack paths and higher vulnerability are considered valid. If the submission is vague or does not identify the attack path with higher severity clearly it will be considered low.
> > 
> > * B is a valid issue
> > * C is low
> 
> The following submissions fail to and/or incorrectly identify the root cause that enables the attack path: #6 #34 #66 #68 #79 #90 #98 #132 #134 #149 .
> 
> * The issues in this category should be Low.
> 
> The following submissions are somewhat vague, but did manage to identify the erroneous storage variable that leads to re-entrancy (`s.index`): #10 #53 #104 #138 #186 (and a few more).
> 
> * While they did not (or vaguely) described the "attack path", the attack path here is just "directly calling `claim()` in your `receive()`", so I suppose one can be ok with just spelling out the function and the wrong storage variable.
> * Since submission quality is subjective, I am flagging these issues so the judges can help with reviewing dupes. Personally I think these submissions are still acceptable, but leaving to the judges to decide the where the bar is.

#134 identifies the issue of how the re-entrance occurs and suggests the same remediation.
It clearly explains the following:
"The vulnerability arises from the contract's failure to update a user's claim state (s.index and s.amountClaimed) before transferring funds to the user, which allows a malicious contract to receive the funds and re-enter the claim function before the original call completes, potentially claiming more funds repeatedly."

The recommendation suggests updating the state before or using a reentrancy guard.

 I am unsure why that has been included in the `low` category per your escalation?  

**midori-fuse**

@Nilay27 I suppose you are right. Sorry about that, there are just too many dupes here, I might have confused it with another issue that got lost somewhere.

But be assured that unless the head of judging downright disagrees with me, all dupes will be reviewed and judged accordingly. Once again I'm sorry for my mistake.

**novaman33**

My issue - #10 does show the root cause clearly and does suggest a thorough recommendation for the mitigation. I do not agree it is vague. 

**keesmark**

It is the same as this one, but why is it considered invalid? #119 

**novaman33**

Probably because #119 says that reentrancy will occur when transferring erc20 tokens while call is used to transfer eth.

**ZdravkoHr**

Also, BNB is out of scope

**Hash01011122**

Acknowledging that every mentioned issue accurately identifies both the root cause of the vulnerability and the correct attack paths, yet noting the straightforward nature of the issue as a reason for minimal effort in Watson's issue, suggests a potential oversight in the importance of comprehensive reporting. 

**shubham-antier**

Issue resolved: Moved the updations above the transfers. Also, added a reentrancy guard to better the security.

**sherlock-admin4**

The protocol team fixed this issue in PR/commit https://github.com/Lithium-Ventures/zap-contracts-labs/pull/2.

**Evert0x**

@Hash01011122 what's your proposal on the exact family for this issue? Which reports should be excluded/included?

**Hash01011122**

@Evert0x Had a indepth review of this family of issues:
Issues which can be excluded are: #6, #10, #34, #66, #79, #90, #132, #138, #149.
The pinpoint the root cause but fail to explain any attack vector.

**armormadeofwoe**

> @Evert0x Had a indepth review of this family of issues: Issues which can be excluded are: #6, #10, #34, #66, #79, #90, #132, #138, #149. The pinpoint the root cause but fail to explain any attack vector.

Hi @Hash01011122, with all due respect, I believe #138 should remain valid since it showcases:
root cause - sending funds before updating variables (breach of CEI pattern)
attack path - the ability to trigger an arbitrary fallback function due to sending native ETH that could re-enter the same function and continue claiming funds due to the unchanged variables. 

I do agree that my report is a little short as this is arguably the most known and recognizable issue in this space, decided to spare the judges some extra reading.

**Hash01011122**

Imao #138 should be excluded as I mentioned above,

**0x3agle**

@Hash01011122 
#6 accurately identifies the root cause and the attack path.
Root cause:
> If the token == address(1) (i.e. the native token) it performs an external call which sends the token to msg.sender and then updates the storage variable.

Attack Path:
> This allows an attacker to reenter the claim function until the contract is drained completely.

**Hash01011122**

@0x3agle with all due respect your report doesn't mention any appropriate Attack Path.

**0x3agle**

@Hash01011122 

Issue: storage variable updated after external call
Attack path: reentering the claim function
Impact: Contract drained
Mitigation: Follow CEI, add non-reentrant

Isn't this enough for this issue to be considered a valid one? 

This issue is so obvious I didn't feel the need for a PoC to convey my point. 

Having said that, I respect your decision and will accept it. 

**Hash01011122**

Hey, if we look from that lens even issues like #10, #34, #66, #132 and #138 should be valid too. I understand what you are pointing even I don't want to invalidate any of the issues as I understand watson's would not spend more effort on writing low hanging fruit issues, However, I'm just adhering to Sherlock's rulebook. Do you want to add anything here @0x3agle?

**Evert0x**

> @Evert0x Had a indepth review of this family of issues: Issues which can be excluded are: #6, #10, #34, #66, #79, #90, #132, #138, #149. The pinpoint the root cause but fail to explain any attack vector.

Planning to accept escalation and move remove the reports mentioned by the Lead Judge as duplicates

**0x3agle**

@Hash01011122 @Evert0x 
You missed #53 and #104

*P.S. I'm not a fan of pulling down other reports but if a selected portion of reports are being disqualified because they didn't mention a "detailed" attack path for an obvious issue, then every report that did not include a detailed description/PoC should be considered for disqualification.*

**novaman33**

@Evert0x could you please identify how #10 fails to explain the attack vector. I believe the attack path is stated clearly and that the solution is also very detailed. 

**Hash01011122**

Agreed, @0x3agle we can add those issues in our list. Updated issues to get excluded will be:
#6, #10, #34, #53, #66, #79, #90, #104, #132, #138, #149 

**Hash01011122**

@novaman33 I don't see any valid attack path mentioned in #10 report.

**Evert0x**

I believe #10 identified the attack pack and shows a good understanding of the issue.

After taken a detailed look at all reports, I believe only the following ones should be excluded as all other reports pinpoint the exact logic in the code that allows the reentrancy to happen. 

https://github.com/sherlock-audit/2024-03-zap-protocol-judging/issues/6, https://github.com/sherlock-audit/2024-03-zap-protocol-judging/issues/34, https://github.com/sherlock-audit/2024-03-zap-protocol-judging/issues/66, https://github.com/sherlock-audit/2024-03-zap-protocol-judging/issues/79, https://github.com/sherlock-audit/2024-03-zap-protocol-judging/issues/90, https://github.com/sherlock-audit/2024-03-zap-protocol-judging/issues/132,  https://github.com/sherlock-audit/2024-03-zap-protocol-judging/issues/149

**Evert0x**

Result:
High
Has Duplicates

**sherlock-admin3**

Escalations have been resolved successfully!

Escalation status:
- [midori-fuse](https://github.com/sherlock-audit/2024-03-zap-protocol-judging/issues/157/#issuecomment-2025184779): accepted

---

## Finding #7: H-3: Signers can bypass checks to add new modules to a safe by abusing reentrancy {#finding-7}

| Property | Value |
|----------|-------|
| **Impact** | HIGH |
| **Quality** | 5/5 |
| **Firm** | Sherlock |
| **Protocol** | Hats |
| **Links** | [GitHub](https://github.com/sherlock-audit/2023-02-hats-judging/issues/41) |

**Found by:** roguereddwarf, obront

---

Source: https://github.com/sherlock-audit/2023-02-hats-judging/issues/41 

## Found by 
obront, roguereddwarf

## Vulnerability Detail

The `checkAfterExecution()` is intended to uphold important invariants after each signer transaction is completed. This is intended to restrict certain dangerous signer behaviors, the most important of which is adding new modules. This was an issue caught in the previous audit and fixed by comparing the hash of the modules before execution to the has of the modules after.

Before:
```solidity
(address[] memory modules,) = safe.getModulesPaginated(SENTINEL_OWNERS, enabledModuleCount);
_existingModulesHash = keccak256(abi.encode(modules));
```

After:
```solidity
(address[] memory modules,) = safe.getModulesPaginated(SENTINEL_OWNERS, enabledModuleCount + 1);
if (keccak256(abi.encode(modules)) != _existingModulesHash) {
    revert SignersCannotChangeModules();
}
```
This is further emphasized in the comments, where it is specified:

> /// @notice Post-flight check to prevent `safe` signers from removing this contract guard, changing any modules, or changing the threshold

### Why Restricting Modules is Important

Modules are the most important thing to check. This is because modules have unlimited power not only to execute transactions but to skip checks in the future. Creating an arbitrary new module is so bad that it is equivalent to the other two issues together: getting complete control over the safe (as if threshold was set to 1) and removing the guard (because they aren't checked in module transactions).

However, this important restriction can be violated by abusing reentrancy into this function.

### Reentrancy Disfunction

To see how this is possible, we first have to take a quick detour regarding reentrancy. It appears that the protocol is attempting to guard against reentrancy with the `guardEntries` variable. It is incremented in `checkTransaction()` (before a transaction is executed) and decremented in `checkAfterExecution()` (after the transaction has completed).

The only protection it provides is in its risk of underflowing, explained in the comments as:

> // leave checked to catch underflows triggered by re-erntry attempts

However, any attempt to reenter and send an additional transaction midstream of another transaction would first trigger the `checkTransaction()` function. This would increment `_guardEntries` and would lead to it not underflowing.

In order for this system to work correctly, the `checkTransaction()` function should simply set `_guardEntries = 1`. This would result in an underflow with the second decrement. But, as it is currently designed, there is no reentrancy protection.

### Using Reentrancy to Bypass Module Check

Remember that the module invariant is upheld by taking a snapshot of the hash of the modules in `checkTransaction()` and saving it in the `_existingModulesHash` variable.

However, imagine the following set of transactions:
- Signers send a transaction via the safe, and modules are snapshotted to `_existingModulesHash`
- The transaction uses the Multicall functionality of the safe, and performs the following actions:
- First, it adds the malicious module to the safe
- Then, it calls `execTransaction()` on itself with any another transaction
- The second call will call `checkTransaction()`
- This will update `_existingModulesHash` to the new list of modules, including the malicious one
- The second call will execute, which doesn't matter (could just be an empty transaction)
- After the transaction, `checkAfterExecution()` will be called, and the modules will match
- After the full transaction is complete, `checkAfterExecution()` will be called for the first transaction, but since `_existingModulesHash` will be overwritten, the module check will pass

## Impact

Any number of signers who are above the threshold will be able to give themselves unlimited access over the safe with no restriction going forward.

## Code Snippet

https://github.com/Hats-Protocol/hats-zodiac/blob/9455cc0957762f5dbbd8e62063d970199109b977/src/HatsSignerGateBase.sol#L495-L498

https://github.com/Hats-Protocol/hats-zodiac/blob/9455cc0957762f5dbbd8e62063d970199109b977/src/HatsSignerGateBase.sol#L522-L525

## Tool used

Manual Review

## Recommendation

Use a more typical reentrancy guard format, such as checking to ensure `_guardEntries == 0` at the top of `checkTransaction()` or simply setting `_guardEntries = 1` in `checkTransaction()` instead of incrementing it.

## Discussion

**zobront**

Escalate for 10 USDC

To successfully duplicate a High Severity issue, it is required for an issue to meet a burden of proof of understanding the exploit. 

#67 clearly meets this burden of proof. It explains the same exploit described in this report and deserves to be duplicated with it.

#105 and #124 do not explain any exploit. They simply noticed that the reentrancy guard wouldn't work, couldn't find a way to take advantage of that, and submitted it without a way to use it. 

My recommendation is that they are not valid issues, but at the very least they should be moved to a separate Medium issue to account for the fact that they did not find a High Severity exploit.

**sherlock-admin**

 > Escalate for 10 USDC
> 
> To successfully duplicate a High Severity issue, it is required for an issue to meet a burden of proof of understanding the exploit. 
> 
> #67 clearly meets this burden of proof. It explains the same exploit described in this report and deserves to be duplicated with it.
> 
> #105 and #124 do not explain any exploit. They simply noticed that the reentrancy guard wouldn't work, couldn't find a way to take advantage of that, and submitted it without a way to use it. 
> 
> My recommendation is that they are not valid issues, but at the very least they should be moved to a separate Medium issue to account for the fact that they did not find a High Severity exploit.

You've created a valid escalation for 10 USDC!

To remove the escalation from consideration: Delete your comment.

You may delete or edit your escalation comment anytime before the 48-hour escalation window closes. After that, the escalation becomes final.

**cducrest**

It's a bit ambitious to have 4 issues describing the same line of codes as incorrect / vulnerable not being marked as duplicate, especially when they provide the same recommendation. I feel like going into such depths to describe the impact may not be necessary to ensure the safety of the protocol. 

However, I agree that it can also feel weird that we would be awarded the same while your issue provides much more details. I could not find anything in the Sherlock docs pertaining to this situation, but maybe there should be a reward for the best issue describing a vulnerability.

When first submitting these issues, I feel like I may take the risk that the issue is treated as medium / low by not providing enough details. Perhaps are you already awarded for having provided such details by ensuring your issue is considered valid?

**hrishibhat**

Escalation accepted

Given that issues #41 & #67 have identified a valid attack path, considering #105 & #124 as a medium as it identifies underlying re-entrancy issue. 

Note: Sherlock will make note of the above comments and discuss internally to add additional instructions in the guide to help resolve such scenarios in the future.

**sherlock-admin**

> Escalation accepted
> 
> Given that issues #41 & #67 have identified a valid attack path, considering #105 & #124 as a medium as it identifies underlying re-entrancy issue. 
> 
> Note: Sherlock will make note of the above comments and discuss internally to add additional instructions in the guide to help resolve such scenarios in the future.

This issue's escalations have been accepted!

Contestants' payouts and scores will be updated according to the changes made on this issue.

---

## Finding #8: H-7: Signers can bypass checks to add new modules to a safe by abusing reentrancy {#finding-8}

| Property | Value |
|----------|-------|
| **Impact** | HIGH |
| **Quality** | 5/5 |
| **Firm** | Sherlock |
| **Protocol** | Hats |
| **Links** | [GitHub](https://github.com/sherlock-audit/2023-02-hats-judging/issues/41) |

**Tags:** `Reentrancy`

**Found by:** roguereddwarf, obront

---

Source: https://github.com/sherlock-audit/2023-02-hats-judging/issues/41 

## Found by 
obront, roguereddwarf

## Vulnerability Detail

The `checkAfterExecution()` is intended to uphold important invariants after each signer transaction is completed. This is intended to restrict certain dangerous signer behaviors, the most important of which is adding new modules. This was an issue caught in the previous audit and fixed by comparing the hash of the modules before execution to the has of the modules after.

Before:
```solidity
(address[] memory modules,) = safe.getModulesPaginated(SENTINEL_OWNERS, enabledModuleCount);
_existingModulesHash = keccak256(abi.encode(modules));
```

After:
```solidity
(address[] memory modules,) = safe.getModulesPaginated(SENTINEL_OWNERS, enabledModuleCount + 1);
if (keccak256(abi.encode(modules)) != _existingModulesHash) {
    revert SignersCannotChangeModules();
}
```
This is further emphasized in the comments, where it is specified:

> /// @notice Post-flight check to prevent `safe` signers from removing this contract guard, changing any modules, or changing the threshold

### Why Restricting Modules is Important

Modules are the most important thing to check. This is because modules have unlimited power not only to execute transactions but to skip checks in the future. Creating an arbitrary new module is so bad that it is equivalent to the other two issues together: getting complete control over the safe (as if threshold was set to 1) and removing the guard (because they aren't checked in module transactions).

However, this important restriction can be violated by abusing reentrancy into this function.

### Reentrancy Disfunction

To see how this is possible, we first have to take a quick detour regarding reentrancy. It appears that the protocol is attempting to guard against reentrancy with the `guardEntries` variable. It is incremented in `checkTransaction()` (before a transaction is executed) and decremented in `checkAfterExecution()` (after the transaction has completed).

The only protection it provides is in its risk of underflowing, explained in the comments as:

> // leave checked to catch underflows triggered by re-erntry attempts

However, any attempt to reenter and send an additional transaction midstream of another transaction would first trigger the `checkTransaction()` function. This would increment `_guardEntries` and would lead to it not underflowing.

In order for this system to work correctly, the `checkTransaction()` function should simply set `_guardEntries = 1`. This would result in an underflow with the second decrement. But, as it is currently designed, there is no reentrancy protection.

### Using Reentrancy to Bypass Module Check

Remember that the module invariant is upheld by taking a snapshot of the hash of the modules in `checkTransaction()` and saving it in the `_existingModulesHash` variable.

However, imagine the following set of transactions:
- Signers send a transaction via the safe, and modules are snapshotted to `_existingModulesHash`
- The transaction uses the Multicall functionality of the safe, and performs the following actions:
- First, it adds the malicious module to the safe
- Then, it calls `execTransaction()` on itself with any another transaction
- The second call will call `checkTransaction()`
- This will update `_existingModulesHash` to the new list of modules, including the malicious one
- The second call will execute, which doesn't matter (could just be an empty transaction)
- After the transaction, `checkAfterExecution()` will be called, and the modules will match
- After the full transaction is complete, `checkAfterExecution()` will be called for the first transaction, but since `_existingModulesHash` will be overwritten, the module check will pass

## Impact

Any number of signers who are above the threshold will be able to give themselves unlimited access over the safe with no restriction going forward.

## Code Snippet

https://github.com/Hats-Protocol/hats-zodiac/blob/9455cc0957762f5dbbd8e62063d970199109b977/src/HatsSignerGateBase.sol#L495-L498

https://github.com/Hats-Protocol/hats-zodiac/blob/9455cc0957762f5dbbd8e62063d970199109b977/src/HatsSignerGateBase.sol#L522-L525

## Tool used

Manual Review

## Recommendation

Use a more typical reentrancy guard format, such as checking to ensure `_guardEntries == 0` at the top of `checkTransaction()` or simply setting `_guardEntries = 1` in `checkTransaction()` instead of incrementing it.

## Discussion

**zobront**

Escalate for 10 USDC

To successfully duplicate a High Severity issue, it is required for an issue to meet a burden of proof of understanding the exploit. 

#67 clearly meets this burden of proof. It explains the same exploit described in this report and deserves to be duplicated with it.

#105 and #124 do not explain any exploit. They simply noticed that the reentrancy guard wouldn't work, couldn't find a way to take advantage of that, and submitted it without a way to use it. 

My recommendation is that they are not valid issues, but at the very least they should be moved to a separate Medium issue to account for the fact that they did not find a High Severity exploit.

**sherlock-admin**

 > Escalate for 10 USDC
> 
> To successfully duplicate a High Severity issue, it is required for an issue to meet a burden of proof of understanding the exploit. 
> 
> #67 clearly meets this burden of proof. It explains the same exploit described in this report and deserves to be duplicated with it.
> 
> #105 and #124 do not explain any exploit. They simply noticed that the reentrancy guard wouldn't work, couldn't find a way to take advantage of that, and submitted it without a way to use it. 
> 
> My recommendation is that they are not valid issues, but at the very least they should be moved to a separate Medium issue to account for the fact that they did not find a High Severity exploit.

You've created a valid escalation for 10 USDC!

To remove the escalation from consideration: Delete your comment.

You may delete or edit your escalation comment anytime before the 48-hour escalation window closes. After that, the escalation becomes final.

**cducrest**

It's a bit ambitious to have 4 issues describing the same line of codes as incorrect / vulnerable not being marked as duplicate, especially when they provide the same recommendation. I feel like going into such depths to describe the impact may not be necessary to ensure the safety of the protocol. 

However, I agree that it can also feel weird that we would be awarded the same while your issue provides much more details. I could not find anything in the Sherlock docs pertaining to this situation, but maybe there should be a reward for the best issue describing a vulnerability.

When first submitting these issues, I feel like I may take the risk that the issue is treated as medium / low by not providing enough details. Perhaps are you already awarded for having provided such details by ensuring your issue is considered valid?

**hrishibhat**

Escalation accepted

Given that issues #41 & #67 have identified a valid attack path, considering #105 & #124 as a medium as it identifies underlying re-entrancy issue. 

Note: Sherlock will make note of the above comments and discuss internally to add additional instructions in the guide to help resolve such scenarios in the future.

**sherlock-admin**

> Escalation accepted
> 
> Given that issues #41 & #67 have identified a valid attack path, considering #105 & #124 as a medium as it identifies underlying re-entrancy issue. 
> 
> Note: Sherlock will make note of the above comments and discuss internally to add additional instructions in the guide to help resolve such scenarios in the future.

This issue's escalations have been accepted!

Contestants' payouts and scores will be updated according to the changes made on this issue.

---

## Finding #9: [H-20] Possibly reentrancy attacks in `_distributeETHRewardsToUserForToken` function {#finding-9}

| Property | Value |
|----------|-------|
| **Impact** | HIGH |
| **Quality** | 0/5 |
| **Firm** | Code4rena |
| **Protocol** | Stakehouse Protocol |
| **Links** | [Source](https://code4rena.com/reports/2022-11-stakehouse) · [GitHub](https://github.com/code-423n4/2022-11-stakehouse-findings/issues/328) |

**Found by:** rotcivegaf, datapunk, 0x4non, clems4ever

---

<https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/SyndicateRewardsProcessor.sol#L51-L73><br>
<https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantMevAndFeesPool.sol#L146-L167><br>
<https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantPoolBase.sol#L66-L90><br>
<https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L66-L104><br>
<https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L110-L143><br>
<https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L314-L340>

The root of the problem is in the `_distributeETHRewardsToUserForToken` which makes a call to distribute the ether rewards. With this call, the recipient can execute an reentrancy attack calling several times the different function to steal founds or take advantage of other users/protocol.

#
#### [`beforeTokenTransfer`, **GiantMevAndFeesPool** contract](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantMevAndFeesPool.sol#L146-L167):

The contract **GiantLP** use the **GiantMevAndFeesPool** contract as [`transferHookProcessor`](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantLP.sol#L14) and when use the functions [`_mint`, `_burn`, `transferFrom` and `transfer` of the ERC20](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v4.7/contracts/token/ERC20/ERC20.sol), the function [`beforeTokenTransfer`](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantMevAndFeesPool.sol#L146-L167) implemented in the **GiantMevAndFeesPool** bring a possibility to make a reentrancy attack because in the function [`_distributeETHRewardsToUserForToken`](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/SyndicateRewardsProcessor.sol#L51-L73) implemented in the [**GiantMevAndFeesPool** make a `call` to the `_recipient`](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/SyndicateRewardsProcessor.sol#L67-L68)

A contract can call the function `transfer` of **GiantLP** contract several time, transfer an `amount` from and to self, as the update of the [`claimed`](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantMevAndFeesPool.sol#L203) would not be done until, it is executed the function [`_afterTokenTransfer`](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantLP.sol#L43-L47) of the **GiantLP** contract, the [`due`](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/SyndicateRewardsProcessor.sol#L61) amount calculated in `_distributeETHRewardsToUserForToken` of **SyndicateRewardsProcessor** contract and the `lastInteractedTimestamp` of **GiantLP** contract will be incorrect

#### [`withdrawLPTokens`, **GiantPoolBase** contract](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantPoolBase.sol#L66-L90):

The possibility of the reentrancy is given when call function [`_onWithdraw`](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantPoolBase.sol#L74), this function implemented in [**GiantMevAndFeesPool** contract](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantMevAndFeesPool.sol#L181-L193) uses `_distributeETHRewardsToUserForToken` and this one call the recipient making the possibility of the reentrancy, breaking the code of [L76-L89](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantPoolBase.sol#L76-L89)

#### [`batchDepositETHForStaking`, **StakingFundsVault** contract](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L66-L104):

The possibility of the reentrancy is given when call function [`_distributeETHRewardsToUserForToken`](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L88-L93), this function call the recipient making the possibility of the reentrancy, breaking the code of [L76-L89](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L96-L107)

#### [`depositETHForStaking`, **StakingFundsVault** contract](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L110-L143):

The possibility of the reentrancy is given when call function [`_distributeETHRewardsToUserForToken`](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L128-L133), this function call the recipient making the possibility of the reentrancy, breaking the code of [L136-L142](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L136-L142)

#### [`beforeTokenTransfer`, **StakingFundsVault** contract](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L314-L340):

The possibility of the reentrancy is given when call function `_distributeETHRewardsToUserForToken` in [L333](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L333) and [L337](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L337), this function call the recipient making the possibility of the reentrancy, breaking the code of [L343-L351](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L343-L351)

### Recommended Mitigation Steps

One possibility is to wrap(`deposit`) ether in WETH and transfer as ERC20 token.

Another is to add `nonReentrant` guard to the functions:

*   [`beforeTokenTransfer`, **GiantMevAndFeesPool** contract](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantMevAndFeesPool.sol#L146-L167)
*   [`withdrawLPTokens`, **GiantPoolBase** contract](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantPoolBase.sol#L66-L90)
*   [`batchDepositETHForStaking`, **StakingFundsVault** contract](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L66-L104)
*   [`depositETHForStaking`, **StakingFundsVault** contract](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L110-L143)
*   [`beforeTokenTransfer`, **StakingFundsVault** contract](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L314-L340)

```diff
File: contracts/liquid-staking/GiantMevAndFeesPool.sol

@@ -143,7 +143,7 @@ contract GiantMevAndFeesPool is ITransferHookProcessor, GiantPoolBase, Syndicate
     }

     /// @notice Allow giant LP token to notify pool about transfers so the claimed amounts can be processed
-    function beforeTokenTransfer(address _from, address _to, uint256) external {
+    function beforeTokenTransfer(address _from, address _to, uint256) external nonReentrant {
         require(msg.sender == address(lpTokenETH), "Caller is not giant LP");
         updateAccumulatedETHPerLP();
```

```diff
File: contracts/liquid-staking/GiantPoolBase.sol

@@ -66,7 +66,7 @@ contract GiantPoolBase is ReentrancyGuard {
     /// @notice Allow a user to chose to withdraw vault LP tokens by burning their giant LP tokens. 1 Giant LP == 1 vault LP
     /// @param _lpTokens List of LP tokens being owned and being withdrawn from the giant pool
     /// @param _amounts List of amounts of giant LP being burnt in exchange for vault LP
-    function withdrawLPTokens(LPToken[] calldata _lpTokens, uint256[] calldata _amounts) external {
+    function withdrawLPTokens(LPToken[] calldata _lpTokens, uint256[] calldata _amounts) external nonReentrant {
         uint256 amountOfTokens = _lpTokens.length;
         require(amountOfTokens > 0, "Empty arrays");
         require(amountOfTokens == _amounts.length, "Inconsistent array lengths");
```

```diff
File: contracts/liquid-staking/StakingFundsVault.sol

@@ -66,7 +66,7 @@ contract StakingFundsVault is
     /// @notice Batch deposit ETH for staking against multiple BLS public keys
     /// @param _blsPublicKeyOfKnots List of BLS public keys being staked
     /// @param _amounts Amounts of ETH being staked for each BLS public key
-    function batchDepositETHForStaking(bytes[] calldata _blsPublicKeyOfKnots, uint256[] calldata _amounts) external payable {
+    function batchDepositETHForStaking(bytes[] calldata _blsPublicKeyOfKnots, uint256[] calldata _amounts) external payable nonReentrant {
         uint256 numOfValidators = _blsPublicKeyOfKnots.length;
         require(numOfValidators > 0, "Empty arrays");
         require(numOfValidators == _amounts.length, "Inconsistent array lengths");

@@ -110,7 +110,7 @@ contract StakingFundsVault is
     /// @notice Deposit ETH against a BLS public key for staking
     /// @param _blsPublicKeyOfKnot BLS public key of validator registered by a node runner
     /// @param _amount Amount of ETH being staked
-    function depositETHForStaking(bytes calldata _blsPublicKeyOfKnot, uint256 _amount) public payable returns (uint256) {
+    function depositETHForStaking(bytes calldata _blsPublicKeyOfKnot, uint256 _amount) public payable nonReentrant returns (uint256) {
         require(liquidStakingNetworkManager.isBLSPublicKeyBanned(_blsPublicKeyOfKnot) == false, "BLS public key is banned or not a part of LSD network");
         require(
             getAccountManager().blsPublicKeyToLifecycleStatus(_blsPublicKeyOfKnot) == IDataStructures.LifecycleStatus.INITIALS_REGISTERED,

@@ -312,7 +312,7 @@ contract StakingFundsVault is
     }

     /// @notice before an LP token is transferred, pay the user any unclaimed ETH rewards
-    function beforeTokenTransfer(address _from, address _to, uint256) external override {
+    function beforeTokenTransfer(address _from, address _to, uint256) external override nonReentrant {
         address syndicate = liquidStakingNetworkManager.syndicate();
         if (syndicate != address(0)) {
             LPToken token = LPToken(msg.sender);
```

**[vince0656 (Stakehouse) confirmed](https://github.com/code-423n4/2022-11-stakehouse-findings/issues/328#issuecomment-1329416775)**

***

---

## Finding #10: [H-20] Possibly reentrancy attacks in _distributeETHRewardsToUserForToken function {#finding-10}

| Property | Value |
|----------|-------|
| **Impact** | HIGH |
| **Quality** | 5/5 |
| **Firm** | Code4rena |
| **Protocol** | Stakehouse Protocol |
| **Links** | [Source](https://code4rena.com/reports/2022-11-stakehouse) · [GitHub](https://github.com/code-423n4/2022-11-stakehouse-findings/issues/328) |

**Tags:** `Reentrancy`

**Found by:** rotcivegaf, datapunk, 0x4non, clems4ever

---

## Lines of code

https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/SyndicateRewardsProcessor.sol#L51-L73
https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantMevAndFeesPool.sol#L146-L167
https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantPoolBase.sol#L66-L90
https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L66-L104
https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L110-L143
https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L314-L340

## Vulnerability details

### Author: rotcivegaf

### Impact

The root of the problem are in the `_distributeETHRewardsToUserForToken` who makes a call to distribute the ether rewards. With this call the recipient can execute an reentrancy attack calling several times the different function to steal founds or take advantage of other users/protocol

#
#### [`beforeTokenTransfer`, **GiantMevAndFeesPool** contract](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantMevAndFeesPool.sol#L146-L167):

The contract **GiantLP** use the **GiantMevAndFeesPool** contract as [`transferHookProcessor`](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantLP.sol#L14) and when use the functions [`_mint`, `_burn`, `transferFrom` and `transfer` of the ERC20](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v4.7/contracts/token/ERC20/ERC20.sol), the function [`beforeTokenTransfer`](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantMevAndFeesPool.sol#L146-L167) implemented in the **GiantMevAndFeesPool** bring a possibility to make a reentrancy attack because in the function [`_distributeETHRewardsToUserForToken`](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/SyndicateRewardsProcessor.sol#L51-L73) implemented in the [**GiantMevAndFeesPool** make a `call` to the `_recipient`](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/SyndicateRewardsProcessor.sol#L67-L68)

A contract can call the function `transfer` of **GiantLP** contract several time, transfer an `amount` from and to self, as the update of the [`claimed`](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantMevAndFeesPool.sol#L203) would not be done until, it is executed the function [`_afterTokenTransfer`](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantLP.sol#L43-L47) of the **GiantLP** contract, the [`due`](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/SyndicateRewardsProcessor.sol#L61) amount calculated in `_distributeETHRewardsToUserForToken` of **SyndicateRewardsProcessor** contract and the `lastInteractedTimestamp` of **GiantLP** contract will be incorrect

### [`withdrawLPTokens`, **GiantPoolBase** contract](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantPoolBase.sol#L66-L90):

The possibility of the reentrancy is given when call function [`_onWithdraw`](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantPoolBase.sol#L74), this function implemented in [**GiantMevAndFeesPool** contract](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantMevAndFeesPool.sol#L181-L193) uses `_distributeETHRewardsToUserForToken` and this one call the recipient making the possibility of the reentrancy, breaking the code of [L76-L89](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantPoolBase.sol#L76-L89)

### [`batchDepositETHForStaking`, **StakingFundsVault** contract](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L66-L104):

The possibility of the reentrancy is given when call function [`_distributeETHRewardsToUserForToken`](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L88-L93), this function call the recipient making the possibility of the reentrancy, breaking the code of [L76-L89](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L96-L107)

### [`depositETHForStaking`, **StakingFundsVault** contract](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L110-L143):

The possibility of the reentrancy is given when call function [`_distributeETHRewardsToUserForToken`](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L128-L133), this function call the recipient making the possibility of the reentrancy, breaking the code of [L136-L142](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L136-L142)

### [`beforeTokenTransfer`, **StakingFundsVault** contract](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L314-L340):

The possibility of the reentrancy is given when call function `_distributeETHRewardsToUserForToken` in [L333](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L333) and [L337](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L337), this function call the recipient making the possibility of the reentrancy, breaking the code of [L343-L351](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L343-L351)

### Tools Used

Review

### Recommended Mitigation Steps

One possibility its wrap(`deposit`) ether in WETH and transfer as ERC20 token

Another, it's add `nonReentrant` guard to the functions:
- [`beforeTokenTransfer`, **GiantMevAndFeesPool** contract](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantMevAndFeesPool.sol#L146-L167)
- [`withdrawLPTokens`, **GiantPoolBase** contract](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/GiantPoolBase.sol#L66-L90)
- [`batchDepositETHForStaking`, **StakingFundsVault** contract](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L66-L104)
- [`depositETHForStaking`, **StakingFundsVault** contract](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L110-L143)
- [`beforeTokenTransfer`, **StakingFundsVault** contract](https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/StakingFundsVault.sol#L314-L340)

```diff
File: contracts/liquid-staking/GiantMevAndFeesPool.sol

@@ -143,7 +143,7 @@ contract GiantMevAndFeesPool is ITransferHookProcessor, GiantPoolBase, Syndicate
     }

     /// @notice Allow giant LP token to notify pool about transfers so the claimed amounts can be processed
-    function beforeTokenTransfer(address _from, address _to, uint256) external {
+    function beforeTokenTransfer(address _from, address _to, uint256) external nonReentrant {
         require(msg.sender == address(lpTokenETH), "Caller is not giant LP");
         updateAccumulatedETHPerLP();
```

```diff
File: contracts/liquid-staking/GiantPoolBase.sol

@@ -66,7 +66,7 @@ contract GiantPoolBase is ReentrancyGuard {
     /// @notice Allow a user to chose to withdraw vault LP tokens by burning their giant LP tokens. 1 Giant LP == 1 vault LP
     /// @param _lpTokens List of LP tokens being owned and being withdrawn from the giant pool
     /// @param _amounts List of amounts of giant LP being burnt in exchange for vault LP
-    function withdrawLPTokens(LPToken[] calldata _lpTokens, uint256[] calldata _amounts) external {
+    function withdrawLPTokens(LPToken[] calldata _lpTokens, uint256[] calldata _amounts) external nonReentrant {
         uint256 amountOfTokens = _lpTokens.length;
         require(amountOfTokens > 0, "Empty arrays");
         require(amountOfTokens == _amounts.length, "Inconsistent array lengths");
```

```diff
File: contracts/liquid-staking/StakingFundsVault.sol

@@ -66,7 +66,7 @@ contract StakingFundsVault is
     /// @notice Batch deposit ETH for staking against multiple BLS public keys
     /// @param _blsPublicKeyOfKnots List of BLS public keys being staked
     /// @param _amounts Amounts of ETH being staked for each BLS public key
-    function batchDepositETHForStaking(bytes[] calldata _blsPublicKeyOfKnots, uint256[] calldata _amounts) external payable {
+    function batchDepositETHForStaking(bytes[] calldata _blsPublicKeyOfKnots, uint256[] calldata _amounts) external payable nonReentrant {
         uint256 numOfValidators = _blsPublicKeyOfKnots.length;
         require(numOfValidators > 0, "Empty arrays");
         require(numOfValidators == _amounts.length, "Inconsistent array lengths");

@@ -110,7 +110,7 @@ contract StakingFundsVault is
     /// @notice Deposit ETH against a BLS public key for staking
     /// @param _blsPublicKeyOfKnot BLS public key of validator registered by a node runner
     /// @param _amount Amount of ETH being staked
-    function depositETHForStaking(bytes calldata _blsPublicKeyOfKnot, uint256 _amount) public payable returns (uint256) {
+    function depositETHForStaking(bytes calldata _blsPublicKeyOfKnot, uint256 _amount) public payable nonReentrant returns (uint256) {
         require(liquidStakingNetworkManager.isBLSPublicKeyBanned(_blsPublicKeyOfKnot) == false, "BLS public key is banned or not a part of LSD network");
         require(
             getAccountManager().blsPublicKeyToLifecycleStatus(_blsPublicKeyOfKnot) == IDataStructures.LifecycleStatus.INITIALS_REGISTERED,

@@ -312,7 +312,7 @@ contract StakingFundsVault is
     }

     /// @notice before an LP token is transferred, pay the user any unclaimed ETH rewards
-    function beforeTokenTransfer(address _from, address _to, uint256) external override {
+    function beforeTokenTransfer(address _from, address _to, uint256) external override nonReentrant {
         address syndicate = liquidStakingNetworkManager.syndicate();
         if (syndicate != address(0)) {
             LPToken token = LPToken(msg.sender);
```

---

## Finding #11: Reentrancy Guard Conflict in `_processVaultRewards` Private Function {#finding-11}

| Property | Value |
|----------|-------|
| **Impact** | HIGH |
| **Quality** | 0/5 |
| **Firm** | Zokyo |
| **Protocol** | Starter |
| **Links** | [Source](https://github.com/solodit/solodit_content/blob/main/reports/Zokyo/2024-06-26-starter.md) |

**Found by:** Zokyo

---

**Severity**: High

**Status**: Resolved

**Location**: CorePool.sol

**Description**

The private function `_processVaultRewards` in `CorePool.sol` is equipped with a `nonReentrant` modifier. This function is called by both internal and external functions that also use the `nonReentrant` modifier, causing a reentrancy guard conflict. Consequently, the function becomes non-executable due to the reentrancy lock it initiates. Adjusting the reentrancy guards or applying a different guard for `_processVaultRewards` is necessary to resolve this issue. This issue potentially leads to loss of funds.

**Recommendation**: 

To resolve the reentrancy guard conflict in `_processVaultRewards`, you can consider the following recommendations:

- **Refactor the Callers**: Ensure that functions calling `_processVaultRewards` manage the reentrancy guard properly. This might involve only applying `nonReentrant` to external or public functions and ensuring that internal functions like `_processVaultRewards` are called in a guarded context.
- **Use Separate Reentrancy Guards**: If necessary, use a different reentrancy guard for `_processVaultRewards` to differentiate it from the guards used by its callers. This can be implemented by creating a new `ReentrancyGuard` instance or using a custom reentrancy mechanism for this function.

By implementing these changes, you can ensure that `_processVaultRewards` executes correctly without encountering reentrancy guard conflicts.

---

## Finding #12: [H-18] Reentrancy attack possible on `RootBridgeAgent.retrySettlement()` with missing access control for `RootBridgeAgentFactory.createBridgeAgent()` {#finding-12}

| Property | Value |
|----------|-------|
| **Impact** | HIGH |
| **Quality** | 0/5 |
| **Firm** | Code4rena |
| **Protocol** | Maia DAO Ecosystem |
| **Links** | [Source](https://code4rena.com/reports/2023-05-maia) · [GitHub](https://github.com/code-423n4/2023-05-maia-findings/issues/492) |

**Found by:** peakbolt, xuwinnie

---

`RootBridgeAgent.retrySettlement()` is lacking a `lock` modifier to prevent reentrancy and `RootBridgeAgentFactory.createBridgeAgent()` is missing access control. Both issues combined allow anyone to re-enter `retrySettlement()` and trigger the same settlement repeatedly.

### Impact

An attacker can steal funds from the protocol by executing the same settlement multiple times before it is marked as executed.

### Issue #1

In `RootBridgeAgentFactory`, the privileged function `createBridgeAgent()` is lacking access control, which allows anyone to deploy a new `RootBridgeAgent`. Leveraging that, the attacker can inject malicious `RootRouter` and `BranchRouter` that can be used to trigger a reentrancy attack in `retrySettlement()`. Injection of the malicious `BranchRouter` is done with a separate call to `CoreRootRouter.addBranchToBridgeAgent()` in [CoreRootRouter.sol#L81-L116](https://github.com/code-423n4/2023-05-maia/blob/main/src/ulysses-omnichain/CoreRootRouter.sol#L81-L116), refer to POC for actual steps.

```Solidity
    function createBridgeAgent(address _newRootRouterAddress) external returns (address newBridgeAgent) {
        newBridgeAgent = address(
            DeployRootBridgeAgent.deploy(
                wrappedNativeToken,
                rootChainId,
                daoAddress,
                local`AnyCall`Address,
                local`AnyCall`ExecutorAddress,
                rootPortAddress,
                _newRootRouterAddress
            )
        );

        IRootPort(rootPortAddress).addBridgeAgent(msg.sender, newBridgeAgent);
    }
```

<https://github.com/code-423n4/2023-05-maia/blob/main/src/ulysses-omnichain/factories/RootBridgeAgentFactory.sol#L75C1-L89C6>

### Issue #2

In `RootBridgeAgent`, the `retrySettlement()` function is not protected from reentrancy with the `lock` modifier. We can then re-enter this function via the injected malicious `BranchRouter` (Issue #1). The malicious `BranchRouter` can be triggered via `BranchBridgeAgentExecutor` when the attacker performs the settlement call. That will execute `IRouter(_router).anyExecuteSettlement()` when additional `calldata` is passed in, as shown in [BranchBridgeAgentExecutor.sol#L110](https://github.com/code-423n4/2023-05-maia/blob/main/src/ulysses-omnichain/BranchBridgeAgentExecutor.sol#L110).

```Solidity
    function retrySettlement(uint32 _settlementNonce, uint128 _remoteExecutionGas) external payable {
        //Update User Gas available.
        if (initialGas == 0) {
            userFeeInfo.depositedGas = uint128(msg.value);
            userFeeInfo.gasToBridgeOut = _remoteExecutionGas;
        }
        //Clear Settlement with updated gas.
        _retrySettlement(_settlementNonce);
    }
```
<https://github.com/code-423n4/2023-05-maia/blob/main/src/ulysses-omnichain/RootBridgeAgent.sol#L244-L252>

#
### Recommended Mitigation Steps

Add a `lock` modifier to `RootBridgeAgent.retrySettlement()` and add access control to `RootBridgeAgentFactory.createBridgeAgent()`.

**[0xBugsy (Maia) confirmed and commented](https://github.com/code-423n4/2023-05-maia-findings/issues/492#issuecomment-1632816163):**
 > Due to a cross-chain tx being composed of several txs on different networks, this would only be feasible on arbitrum, since it's the only chain where both `root` and `branch` contracts co-exist; allowing you to nest new retrys inside the previous. Otherwise, the nonce would be flagged as executed in the execution history after the first successful run. But definitely the `lock` should be added.

**[0xBugsy (Maia) commented](https://github.com/code-423n4/2023-05-maia-findings/issues/492#issuecomment-1641038311):**
 > To give a little further context on my reply: 
> 
> 1. The permissionless addition of `Bridge Agent` does not expose any unintended functions to the `Router`, so this part is completely intended on our behalf.
> 
> 2. The core issue here, really resides on the fact that the `executionHistory[nonce] = true;` should be done in the `Branch` and `Root` `Bridge Agents` before and not after (respecting CEI), calling their respective `Executor` within a try-catch block. Adding a `lock` can also be introduced as a safe-guard, but adding that by itself we would still be able to do this attack once within the original settlement.

**[0xLightt (Maia) commented](https://github.com/code-423n4/2023-05-maia-findings/issues/492#issuecomment-1709165849):**
> Addressed [here](https://github.com/Maia-DAO/eco-c4-contest/tree/183-492-688-869).

***

---

## Finding #13: [H-05] Reentrancy in LiquidStakingManager.sol#withdrawETHForKnow leads to loss of fund from smart wallet {#finding-13}

| Property | Value |
|----------|-------|
| **Impact** | HIGH |
| **Quality** | 4.333333333333333/5 |
| **Firm** | Code4rena |
| **Protocol** | Stakehouse Protocol |
| **Links** | [Source](https://code4rena.com/reports/2022-11-stakehouse) · [GitHub](https://github.com/code-423n4/2022-11-stakehouse-findings/issues/110) |

**Tags:** `Reentrancy`

**Found by:** Trust, bitbopper, yixxas, 0xbepresent, ladboy233, btk

---

## Lines of code

https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/LiquidStakingManager.sol#L435
https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/LiquidStakingManager.sol#L326
https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/LiquidStakingManager.sol#L340
https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/LiquidStakingManager.sol#L347

## Vulnerability details

## Impact

Reentrancy in LiquidStakingManager.sol#withdrawETHForKnow leads to loss of fund from smart wallet

## Tools Used

Manual Review

## Recommended Mitigation Steps

We recommend ban the public key first then send the fund out, and use openzeppelin nonReentrant modifier to avoid reentrancy.

```solidity

// update the mapping
bannedBLSPublicKeys[_blsPublicKeyOfKnot] = associatedSmartWallet;

// refund 4 ether from smart wallet to node runner's EOA
IOwnableSmartWallet(associatedSmartWallet).rawExecute(
	_recipient,
	"",
	4 ether
);
```

---

## Finding #14: Reentrancy in `EscrowManager` {#finding-14}

| Property | Value |
|----------|-------|
| **Impact** | HIGH |
| **Quality** | 0/5 |
| **Firm** | MixBytes |
| **Protocol** | EYWA |
| **Links** | [Source](https://github.com/mixbytes/audits_public/blob/master/EYWA/DAO/README.md#4-reentrancy-in-escrowmanager) |

**Tags:** `Reentrancy`

**Found by:** MixBytes

---

##### Description

OpenZeppelin ERC721 NFT implementations invoke the receiver whenever the `safeTransferFrom()` or `safeMint()` methods are called.

A hacker can exploit this mechanism by triggering a callback from `EscrowManager` during the execution of methods such as `createLock()` (when `_safeMint()` is invoked), `deboost()` (when `safeTransferFrom()` is invoked), and `withdraw()` (also when `safeTransferFrom()` is invoked), especially when the state of `EscrowManager` is inconsistent. This can corrupt storage variables or result in voting power gain.

**Example 1**: Reentrancy in the `deboost()` method with duplicate boosters.

An attacker can exploit a reentrancy vulnerability in the `deboost()` method, manipulating the boosting mechanism to their advantage:
1. The attacker calls the `deboost()` method and passes the same boosting NFT ID multiple times, e.g., `deboost(escrowId, [1,1,1,1,1,1,1,1])`.
2. During the transfer process, the `deboost()` method triggers a callback to the attacker’s contract.
3. Each time the attacker’s contract receives the NFT, it transfers the NFT back to `EscrowManager`.

As a result, the escrow boosting coverage can be reduced to zero, even though other boosting NFTs may still be present and not withdrawn. This makes subsequent calculations inaccurate, disproportionately **inflating** the attacker’s `lockAmount` and voting power.

```
Hacker votes before deboost: 4402998660126770n
Hacker votes after  deboost: 1105121050824042828n
```

*[Long code block removed]*

Second, the hacker's contract:

*[Long code block removed]*

**Example 2**: A hacker can corrupt storage variables via `createLock()` and `withdraw()` methods.

**Attack Scenario:**
1. The attacker calls the `createLock()` method to mint a new NFT lock.
2. During the `_safeMint()` process, the `ERC721Utils.checkOnERC721Received()` callback is triggered on the attacker’s contract.
3. Within this callback, the attacker calls `EscrowManager.withdraw()`, burning the newly minted NFT. 
4. At this point, the NFT’s state has not yet been fully updated in the `createLock()` function, allowing the attacker to corrupt the **totalLocked** value.

This altered **totalLocked** value could distort token emission calculations in the `emissionManager` contract, leading to unfair or excessive token distributions.

##### Recommendation

We recommend using the following approaches against reentrancy:
1. Use Check-Effect-Interaction pattern when minting, burning or transferring NFTs.
2. Use reentrancy guard modifiers.
3. Use methods that do not cause an unintentional callback.

***

---

## Finding #15: Malicious User Can Drain Rewards Through Reentrancy in Staking {#finding-15}

| Property | Value |
|----------|-------|
| **Impact** | HIGH |
| **Quality** | 0/5 |
| **Firm** | Quantstamp |
| **Protocol** | Zero Staking |
| **Links** | [Source](https://certificate.quantstamp.com/full/zero-staking/40ffa176-7b8d-43ec-a7e2-29732c12f21e/index.html) |

**Found by:** Jennifer Wu, Julio Aguilar, Jeffrey Kam

---

**Update**
Marked as "Fixed" by the client. Addressed in: `0a9a94bb49ec54fce5e6bd8859be3f981fbbac4a`.

**File(s) affected:**`StakingERC20.sol`, `StakingERC721.sol`

**Description:** The `StakingERC721.stake()` function allows a malicious staker to exploit the stale `staker.lastUpdatedTimestamp` due to a reentrancy vulnerability. During the staking process, the `_stake()` function calls `_safeMint()`, which calls `checkOnERC721Received()`. This allows the staker to re-enter the staking contract during the minting process. Since the `staker.lastUpdatedTimestamp` is only updated at the end of the `stake()` function, the staker can re-enter the `stake()` or `unstake()` function to trigger multiple `_checkRewards` calculations, thereby unfairly increasing their pending rewards based on the `staker.lastUpdatedTimestamp`.

Similar reentrancy risks exist in the `StakingERC20.stake()` function if ERC777 tokens are accepted as staking tokens. The ERC777 token standard was created to extend the capabilities available in ERC20 tokens and one of the features allows the ERC777 token contract to notify the sender and recipient when ERC777 tokens are sent or received, which a malicious staker can use to re-enter the staking function.

**Recommendation:** Implement reentrancy protection in the `stake()` and `unstake()` functions to prevent users from re-entering the functions and exploiting the stale `lastUpdatedTimestamp`. This can be achieved using a reentrancy guard, such as OpenZeppelin's `ReentrancyGuard`, or by updating the `staker.lastUpdatedTimestamp` earlier:

1.   **Use Reentrancy Guard:** Add the `nonReentrant` modifier to the `stake()` and `unstake()` functions to prevent reentrancy.
2.   **Update Timestamp Early:** Update the `staker.lastUpdatedTimestamp` before calling any external functions to ensure that the timestamp is accurate and up-to-date before any potential reentrant calls can occur.

---

## Finding #16: Reentrancy attack to duplicate NFT tier to other contracts  {#finding-16}

| Property | Value |
|----------|-------|
| **Impact** | HIGH |
| **Quality** | 0/5 |
| **Firm** | Cantina |
| **Protocol** | Trugly Labs |
| **Links** | [Source](https://cdn.cantina.xyz/reports/cantina_managed_trugly_jun2024.pdf) · [PDF](https://solodit-bucket.s3.amazonaws.com/storage/reports/cantina/cantina_managed_trugly_jun2024.pdf) |

**Found by:** slowfi, Jonatas Martins

---

## Vulnerability Report: Reentrancy Attack in _mintTier() Function

## Context
**File:** MEME404.sol#L261

## Description
When minting a tier through the `_mintTier()` function, a callback function is used when dealing with ERC1155 tokens. This callback is invoked when `_checkERC1155Received()` is called.

```solidity
if ((_owner.code.length != 0) && !_checkERC1155Received(_owner, msg.sender, address(0), tier.lowerId, 1)) {
    return;
}
```

A **reentrancy attack** is possible through the `_mintTier()` function. In this case, an attacker can duplicate their tier to other contracts, minting NFTs to these contracts without holding any MEME404 tokens. This reentrancy attack is only possible when using MEME1155 as a tier.

### Path to Execute the Attack
1. Attacker creates a contract to hold the duplicated 1155 with the `onERC1155Received`.
2. Attacker transfers all tokens to the contract created.
3. Through the reentrancy, the contract sends all tokens back to the attacker before finishing the execution of minting.
4. The attacker and the contract have now the same tier.

As a result, the contract doesn't hold any token but could break any integration that requires a tier for a contract.

## Recommendation
Add the OZ ReentrancyGuard to the functions.

## Status
- **Trugly Labs:** Fixed in commit 05c9bf31.
- **Cantina Managed:** Fixed.

---

## Finding #17: Reentrancy in StEthHyperdrive.openShort {#finding-17}

| Property | Value |
|----------|-------|
| **Impact** | HIGH |
| **Quality** | 0/5 |
| **Firm** | Spearbit |
| **Protocol** | Hyperdrive June 2023 |
| **Links** | [Source](https://github.com/spearbit/portfolio/blob/master/pdfs/Delv-Spearbit-Security-Review-June-2023.pdf) · [PDF](https://solodit-bucket.s3.amazonaws.com/storage/reports/spearbit/Delv-Spearbit-Security-Review-June-2023.pdf) |

**Found by:** Saw-Mon and Natalie, Christoph Michel, Deivitto, M4rio.eth

---

## Critical Risk Assessment

## Severity
**Critical Risk**

## Context
- **Files:** HyperdriveShort.sol#L89, StethHyperdrive.sol#L73

## Description
The `StethHyperdrive._deposit` function contains refund logic which performs a `.call` to the `msg.sender`. When opening shorts, this `_deposit` with the callback happens in the middle of state updates, which can be abused by an attacker. The `_deposit` occurs after calculating the short reserves updates (`_calculateOpenShort`) but before applying these updates to the reserves. 

When the attacker receives the callback, they can trade on the same curve with the same reserves a second time, allowing them to achieve better price execution (incurring less slippage) than a single large trade. 

In the proof of concept, the attacker opens half the short initially and half through reentrancy, then immediately closes the total short amount for profit, draining the pool funds.

### Changes to `MockHyperdrive`:

```solidity
function _deposit(uint256 amount, bool) internal override returns (uint256, uint256) {
    _callback();
    uint256 assets = _baseToken.balanceOf(address(this));
    bool success = _baseToken.transferFrom(msg.sender, address(this), amount);
    if (!success) {
        revert Errors.TransferFailed();
    }
    if (totalShares == 0) {
        totalShares = amount;
        return (amount, FixedPointMath.ONE_18);
    } else {
        uint256 newShares = totalShares.mulDivDown(amount, assets);
        totalShares += newShares;
        return (newShares, _pricePerShare());
    }
}

function _callback() internal {
    // I added this to simulate the ETH refund callback in `StEthHyperdrive`.
    // NOTE: we are doing the callback before `transferFrom` to simulate the share price not
    // changing as the StEthHyperdrive callback happens before submitting to Lido and leaves its
    // share price unchanged, `lido.getTotalPooledEther().divDown(lido.getTotalShares())`. If we do
    // it in between the `transferFrom` and `totalShares` update in the Mock, it will change the
    // share price, which would not simulate StEthHyperdrive (or any atomic deposit).

    (bool success,) = payable(msg.sender).call{value: 0}("");
    if (!success) {
        revert Errors.TransferFailed();
    }
}
```

## Test

*[Long code block removed]*

## Output

## Recommendation
Consider fixing the reentrancy in the middle of a state update. Either remove the refund logic in `_deposit` and add the refund logic only at the end of `openShort` after all updates have been done. Alternatively, consider adding reentrancy guards to all public functions. The reentrancy flag could be in the same storage slot as the pause flag for gas efficiency.

**Warning:** In case the reentrancy lock is not implemented, future Hyperdrive developments need to ensure that no similar attack vector is exposed.

---

## Finding #18: RocketNodeDistributorDelegate - Reentrancy in distribute() allows node owner to drain distributor funds ✓ Fixed {#finding-18}

| Property | Value |
|----------|-------|
| **Impact** | HIGH |
| **Quality** | 5/5 |
| **Firm** | ConsenSys |
| **Protocol** | Rocket Pool Atlas (v1.2) |
| **Links** | [Source](https://consensys.net/diligence/audits/2023/01/rocket-pool-atlas-v1.2/) |

**Tags:** `Reentrancy`

**Found by:** Dominik Muhs,  Martin Ortner


---

#### Resolution

Fixed in <https://github.com/rocket-pool/rocketpool/tree/77d7cca65b7c0557cfda078a4fc45f9ac0cc6cc6> by implementing a custom reentrancy guard via a new state variable `lock` that is appended to the end of the storage layout. The reentrancy guard is functionally equivalent to the OpenZeppelin implementation. The method was not refactored to give user funds priority over the node share. Additionally, the client provided the following statement:

> 
> We acknowledge this as a critical issue and have solved with a reentrancy guard.
> 
> 
> 

> 
> We followed OpenZeppelin’s design for a reentrancy guard. We were unable to use it directly as it is hardcoded to use storage slot 0 and because we already have deployment of this delegate in the wild already using storage slot 0 for another purpose, we had to append it to the end of the existing storage layout.
> 
> 
> 

#### Description

The `distribute()` function distributes the contract’s balance between the node operator and the user. The node operator is returned their initial collateral, including a fee. The rest is returned to the RETH token contract as user collateral.

After determining the node owner’s share, the contract transfers `ETH` to the node withdrawal address, which can be the configured withdrawal address or the node address. Both addresses may potentially be a malicious contract that recursively calls back into the `distribute()` function to retrieve the node share multiple times until all funds are drained from the contract. The `distribute()` function is not protected against reentrancy:

**code/contracts/contract/node/RocketNodeDistributorDelegate.sol:L59-L73**

```
/// @notice Distributes the balance of this contract to its owners
function distribute() override external {
    // Calculate node share
    uint256 nodeShare = getNodeShare();
    // Transfer node share
    address withdrawalAddress = rocketStorage.getNodeWithdrawalAddress(nodeAddress);
    (bool success,) = withdrawalAddress.call{value : nodeShare}("");
    require(success);
    // Transfer user share
    uint256 userShare = address(this).balance;
    address rocketTokenRETH = rocketStorage.getAddress(rocketTokenRETHKey);
    payable(rocketTokenRETH).transfer(userShare);
    // Emit event
    emit FeesDistributed(nodeAddress, userShare, nodeShare, block.timestamp);
}

```
We also noticed that any address could set a withdrawal address as there is no check for the caller to be a registered node. In fact, the caller can be the withdrawal address or node operator.

**code/contracts/contract/RocketStorage.sol:L118-L133**

```
// Set a node's withdrawal address
function setWithdrawalAddress(address \_nodeAddress, address \_newWithdrawalAddress, bool \_confirm) external override {
    // Check new withdrawal address
    require(\_newWithdrawalAddress != address(0x0), "Invalid withdrawal address");
    // Confirm the transaction is from the node's current withdrawal address
    address withdrawalAddress = getNodeWithdrawalAddress(\_nodeAddress);
    require(withdrawalAddress == msg.sender, "Only a tx from a node's withdrawal address can update it");
    // Update immediately if confirmed
    if (\_confirm) {
        updateWithdrawalAddress(\_nodeAddress, \_newWithdrawalAddress);
    }
    // Set pending withdrawal address if not confirmed
    else {
        pendingWithdrawalAddresses[\_nodeAddress] = \_newWithdrawalAddress;
    }
}

```
#### Recommendation

Add a reentrancy guard to functions that interact with untrusted contracts. Adhere to the checks-effects pattern and send user funds to the ‘trusted’ RETH contract first. Only then send funds to the node’s withdrawal address.

---

## Finding #19: [H-05] Reentrancy in `LiquidStakingManager.sol#withdrawETHForKnow` leads to loss of fund from smart wallet {#finding-19}

| Property | Value |
|----------|-------|
| **Impact** | HIGH |
| **Quality** | 0/5 |
| **Firm** | Code4rena |
| **Protocol** | Stakehouse Protocol |
| **Links** | [Source](https://code4rena.com/reports/2022-11-stakehouse) · [GitHub](https://github.com/code-423n4/2022-11-stakehouse-findings/issues/110) |

**Found by:** Trust, bitbopper, yixxas, 0xbepresent, ladboy233, btk

---

<https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/LiquidStakingManager.sol#L435><br>
<https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/LiquidStakingManager.sol#L326><br>
<https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/LiquidStakingManager.sol#L340><br>
<https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/contracts/liquid-staking/LiquidStakingManager.sol#L347><br>

The code below violates the check effect pattern, the code banned the public key to mark the public key invalid to not let the msg.sender withdraw again after sending the ETH.

```solidity
    /// @notice Allow node runners to withdraw ETH from their smart wallet. ETH can only be withdrawn until the KNOT has not been staked.
    /// @dev A banned node runner cannot withdraw ETH for the KNOT. 
    /// @param _blsPublicKeyOfKnot BLS public key of the KNOT for which the ETH needs to be withdrawn
    function withdrawETHForKnot(address _recipient, bytes calldata _blsPublicKeyOfKnot) external {
        require(_recipient != address(0), "Zero address");
        require(isBLSPublicKeyBanned(_blsPublicKeyOfKnot) == false, "BLS public key has already withdrawn or not a part of LSD network");

        address associatedSmartWallet = smartWalletOfKnot[_blsPublicKeyOfKnot];
        require(smartWalletOfNodeRunner[msg.sender] == associatedSmartWallet, "Not the node runner for the smart wallet ");
        require(isNodeRunnerBanned(nodeRunnerOfSmartWallet[associatedSmartWallet]) == false, "Node runner is banned from LSD network");
        require(associatedSmartWallet.balance >= 4 ether, "Insufficient balance");
        require(
            getAccountManager().blsPublicKeyToLifecycleStatus(_blsPublicKeyOfKnot) == IDataStructures.LifecycleStatus.INITIALS_REGISTERED,
            "Initials not registered"
        );

        // refund 4 ether from smart wallet to node runner's EOA
        IOwnableSmartWallet(associatedSmartWallet).rawExecute(
            _recipient,
            "",
            4 ether
        );

        // update the mapping
        bannedBLSPublicKeys[_blsPublicKeyOfKnot] = associatedSmartWallet;

        emit ETHWithdrawnFromSmartWallet(associatedSmartWallet, _blsPublicKeyOfKnot, msg.sender);
    }
```

Note the section:

```solidity
// refund 4 ether from smart wallet to node runner's EOA
IOwnableSmartWallet(associatedSmartWallet).rawExecute(
	_recipient,
	"",
	4 ether
);

// update the mapping
bannedBLSPublicKeys[_blsPublicKeyOfKnot] = associatedSmartWallet;
```

If the \_recipient is a smart contract, it can re-enter the withdraw function to withdraw another 4 ETH multiple times before the public key is banned.

As shown in our running POC.

We need to add the import first:

```solidity
import { MockAccountManager } from "../../contracts/testing/stakehouse/MockAccountManager.sol";
```

We can add the smart contract below:

<https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/test/foundry/LiquidStakingManager.t.sol#L12>

*[Long code block removed]*

There is a restriction in this reentrancy attack, the msg.sender needs to be the same recipient when calling `withdrawETHForKnot`.

We add the test case.

<https://github.com/code-423n4/2022-11-stakehouse/blob/4b6828e9c807f2f7c569e6d721ca1289f7cf7112/test/foundry/LiquidStakingManager.t.sol#L35>

```solidity
function testBypassIsContractCheck_POC() public {

	NonEOARepresentative pass = new NonEOARepresentative{value: 8 ether}(address(manager));
	address wallet = manager.smartWalletOfNodeRunner(address(pass));
	address reprenstative = manager.smartWalletRepresentative(wallet);
	console.log("smart contract registered as a EOA representative");
	console.log(address(reprenstative) == address(pass));

	// to set the public key state to IDataStructures.LifecycleStatus.INITIALS_REGISTERED
	MockAccountManager(factory.accountMan()).setLifecycleStatus("publicKeys1", 1);

	// expected to withdraw 4 ETHER, but reentrancy allows withdrawing 8 ETHER
	pass.withdraw("publicKeys1");
	console.log("balance after the withdraw, expected 4 ETH, but has 8 ETH");
	console.log(address(pass).balance);

}
```

We run the test:

```solidity
forge test -vv --match testWithdraw_Reentrancy_POC
```

And the result is

```solidity
Running 1 test for test/foundry/LiquidStakingManager.t.sol:LiquidStakingManagerTests

Logs:
  smart contract registered as a EOA representative
  true
  balance after the withdraw, expected 4 ETH, but has 8 ETH
  8000000000000000000

Test result: ok. 1 passed; 0 failed; finished in 14.85ms
```

The function call is

`pass.withdraw("publicKeys1")`, which calls

```solidity
function withdraw(bytes calldata _blsPublicKeyOfKnot) external {
	IManager(manager).withdrawETHForKnot(address(this), _blsPublicKeyOfKnot);
}
```

Which trigger:

```solidity
// refund 4 ether from smart wallet to node runner's EOA
IOwnableSmartWallet(associatedSmartWallet).rawExecute(
	_recipient,
	"",
	4 ether
);
```

Which triggers reentrancy to withdraw the fund again before the public key is banned.

```solidity
receive() external payable {
	if(!state) {
		state = true;
		this.withdraw("publicKeys1");
	}
}
```

### Recommended Mitigation Steps

We recommend ban the public key first then send the fund out, and use openzeppelin nonReentrant modifier to avoid reentrancy.

```solidity

// update the mapping
bannedBLSPublicKeys[_blsPublicKeyOfKnot] = associatedSmartWallet;

// refund 4 ether from smart wallet to node runner's EOA
IOwnableSmartWallet(associatedSmartWallet).rawExecute(
	_recipient,
	"",
	4 ether
);
```

**[vince0656 (Stakehouse) confirmed](https://github.com/code-423n4/2022-11-stakehouse-findings/issues/110)**

***

---

## Finding #20: Reentrancy Vulnerability Allows Draining All Funds {#finding-20}

| Property | Value |
|----------|-------|
| **Impact** | HIGH |
| **Quality** | 0/5 |
| **Firm** | SigmaPrime |
| **Protocol** | Sushi |
| **Links** | [Source](https://github.com/sigp/public-audits/blob/master/sushi/bentobox-strategies-staking-contract/review.pdf) · [PDF](https://solodit-bucket.s3.amazonaws.com/storage/reports/sigmaprime/bentobox-strategies-staking-contract.pdf) |

**Tags:** `Reentrancy`

**Found by:** Sigma Prime

---

## Description

A reentrancy vulnerability in the function `stakeToken()` allows an attacker to drain the funds of any ERC20 token deposited in the contract.

In `stakeToken()` on line [180], `msg.sender`’s liquidity is updated in the state variable `userStakes`, however the incentive’s total liquidity is not updated until line [202]. In between, on line [194], there is a call to `_claimReward()` which passes execution flow back to the token being transferred. Using a malicious token that can react to transfers, such as an ERC777 token, or a custom attack token, the attacker can reenter the contract in between these two lines and interact with the contract in a partially updated state.

In the partially updated state, `userStake.liquidity` has been increased but the total liquidity of one or more incentives have not been. `userStake.liquidity` is global across all the user’s incentives and is used as a multiplier when rewards are calculated. Therefore, a malicious user may multiply the rewards for unclaimed incentives by an inflated figure and drain tokens.

The steps taken for this attack are as follows, suppose that there are multiple incentives where USDC is the staking token. Bob is the attacker and has created a malicious token contract, ATT.

1. Bob creates an incentive staking USDC for rewards in ATT.
2. Bob deposits some USDC into multiple target incentives and also into his ATT incentive. All target incentives must be staking USDC for some other token. It is these other tokens that will be drained. The order of subscriptions is also important. The ATT incentive needs to be first.
3. Bob waits for some rewards to accumulate.
4. Bob takes a flash loan of USDC and calls `stakeToken()` to deposit the flash loan with the parameter `transferExistingRewards` as `True`. As the staking contract loops through the incentives that Bob is subscribed to on line [184], it calls the ATT incentive first (as Bob has been careful to subscribe in the correct order for this to happen).
5. When ATT’s `safeTransfer()` function is called, it passes execution control to Bob, allowing reentrancy. Bob calls `claimRewards()` for the other incentives he is subscribed to. The reward multiplier `usersLiquidity` on line [378] will be out of proportion to the overall liquidity and this can result in the staking contract paying out its entire balance of the reward token.
6. Bob calls `unstakeToken()` to get back the flash loan and repays it.

A similar reentrancy vulnerability occurs using `_claimReward()` which instead reenters the function `unsubscribeFromIncentive()` and may overflow the unchecked operation on the following line.

```solidity
unchecked { incentive.liquidityStaked -= userStake.liquidity; }
```

## Recommendations

There are two preventive measures that may be taken to mitigate reentrancy:

1. Carefully implement the checks->effects->interaction pattern throughout `StakingContractMainnet`. In particular, make sure that it is not being violated within function calls. This ensures that all external calls are made after state updates.
   
2. Use a reentrancy guard, the best known of which is OpenZeppelin’s `ReentrancyGuard`, and apply its modifier `nonReentrant()` on all public and external functions.

This reentrancy protection will also prevent against the unchecked overflow on line [286]. In that case, consider also removing the unchecked wrapper to allow for overflow protection in the two functions `unsubscribeFromIncentive()` and `unstakeToken()`. The gas increase of using checked math is small for these two variables and the added security significant.

## Resolution

This issue was resolved by using the Solmate re-entrancy guard. The fix is outlined in PR 1.

---

## End of Report

**Total Findings:** 20

**Generated:** 2026-02-04 04:22:25
