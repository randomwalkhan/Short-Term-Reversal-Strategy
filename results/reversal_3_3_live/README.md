# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-15 15:20:01 EDT`
Last processed slot: `manage_1530`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$14,083.25`
- Equity: `$26,388.25`
- Realized PnL: `$17,308.25`
- Unrealized PnL: `$-920.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ROST     option         option ROST260717C00240000       2026-06-15                   0     23     13225.0                 12305.0         5.75           5.35      236.66        236.66          bid_ask_mid                       5.35                bid_ask_mid                    True          -920.0                  -6.96         91.67               12              1.45         26.78           24.98                  38.75                 169.0           31.0               0.12                      ok
```

## Today's Closed Trades (2026-06-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ROST           91.67               12            1.45              2.43        239.09                38.75         0.621          pass              0.444             19.1                           0.274                5.83              0.610                                 ok            True                  False
  CPRT           84.62               13            2.03              0.44         30.56                31.00         0.528          pass              0.212              5.3                           0.199               -6.79             -0.224                                 ok            True                  False
   BKR           82.35               34            0.79              0.35         62.99                39.91         0.510          pass              0.485             70.5                           0.646               -0.52             -0.200                                 ok            True                  False
  CTAS           96.00               25            1.04              1.28        175.73                29.28         0.508          pass              0.660             36.5                           0.399                0.90              0.237                                 ok            True                  False
  AMGN           92.86               28            0.55              1.37        354.61                28.14         0.504          pass              0.682             56.2                           0.469                7.33              0.672                                 ok            True                  False
   KHC          100.00                3            1.07              0.18         24.31                26.17         0.668          pass              0.530             21.2                           0.420                3.97              0.782                                 ok           False                  False
   TRI           80.77               26            0.57              0.33         81.27                63.37         0.645          pass              0.313             40.4                           0.473              -13.85             -1.151 downtrend_blocked_slope_and_streak           False                  False
  WDAY           84.85               33            1.20              1.10        130.33                70.45         0.556          pass              0.422             28.1                           0.412              -17.81             -1.897 downtrend_blocked_slope_and_streak           False                  False
   ADP           95.24               21            1.50              2.38        225.19                32.50         0.548          pass              0.565             12.1                           0.257               -4.68             -0.316            downtrend_blocked_slope           False                  False
  MDLZ           75.00                4            2.06              0.91         62.60                19.17         0.540          pass              0.109             18.5                           0.506                1.05              0.348                                 ok           False                  False
  DXCM           78.95               19            1.82              0.96         74.96                46.69         0.527          pass              0.188             25.2                           0.397               -1.17              0.214                                 ok           False                  False
 CMCSA           75.00               12            1.65              0.28         24.38                24.55         0.525          pass              0.090              8.0                           0.325               -3.81             -0.142                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et       slot     event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-06-15T15:10:06.131512-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-15T15:05:05.449965-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-15T15:00:05.161177-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-15T14:55:01.106139-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-15T14:50:01.113692-04:00 entry_1500          entry {"allocated_cash": 13225.0, "asset_type": "option", "contract_symbol": "ROST260717C00240000", "contracts": 23, "early_entry_score": 0.444, "entry_mode": "regular", "entry_option_price": 5.75, "execution_mode": "option", "matched_signals": 12, "option_liquidity_status": "ok", "option_open_interest": 169.0, "option_spread_pct": 12.17, "option_volume": 31.0, "success_rate": 91.67, "ticker": "ROST", "timing_score": 0.621}
2026-06-15T14:50:01.113692-04:00 entry_1500 timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-15", "training_samples": 5261, "window": 5}
2026-06-12T15:10:11.830500-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-12T15:05:11.809096-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-12T15:00:11.776390-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-12T14:55:11.337200-04:00 entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260615152001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260615152001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260615152001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260615152001)

</details>
