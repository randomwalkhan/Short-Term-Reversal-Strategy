# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-12 10:30:01 EDT`
Last processed slot: `manage_1030`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$17,853.50`
- Equity: `$33,778.50`
- Realized PnL: `$25,353.50`
- Unrealized PnL: `$-1,575.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00520000       2026-05-12                   0      5     17500.0                 15925.0         35.0          31.85       510.5        513.41         -1575.0                   -9.0         96.97               33               1.1          1.56           53.09                  42.97                 202.0           13.0                0.0                      ok
```

## Today's Closed Trades (2026-05-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           88.10               42            0.95              0.58         87.06               115.89         0.699          pass              0.672             61.9                           0.548               24.06              2.563                                 ok            True                  False
  GOOG           87.10               31            0.82              2.22        385.82                39.86         0.562          pass              0.483             32.5                           0.401               10.39              1.043                                 ok            True                  False
    ZS           82.86               35            1.04              1.08        148.41                59.15         0.532          pass              0.424             42.6                           0.463                8.27              1.273                                 ok            True                  False
  CDNS           96.55               29            1.43              3.64        362.64                37.36         0.518          pass              0.658             26.6                           0.392               10.36              1.164                                 ok            True                  False
   CSX           85.19               27            0.89              0.28         44.62                30.07         0.518          pass              0.370             22.3                           0.283               -1.97             -0.130                                 ok            True                  False
   XEL           95.65               23            0.79              0.44         80.41                27.14         0.509          pass              0.763             75.0                           0.649                0.61             -0.063                                 ok            True                  False
  ASML           85.71               14            3.40             37.25       1549.84                49.29         0.508          pass              0.257              9.1                           0.273                9.25              1.304                                 ok            True                  False
   TXN           88.89                9            2.39              4.99        295.62                67.69         0.696          pass              0.354             15.9                           0.369               10.23              0.951                                 ok           False                  False
 CMCSA           94.12               34            0.18              0.03         25.02                62.25         0.664          pass              0.844             80.4                           0.535               -9.61             -0.968 downtrend_blocked_slope_and_streak           False                  False
  NXPI           69.23               13            3.23              6.92        303.03                87.21         0.621          pass              0.259             59.0                           0.519               28.53              1.346                                 ok           False                  False
  FTNT           95.45               44            0.39              0.32        115.30                70.54         0.571          pass              0.880             74.4                           0.793               34.14              3.632                                 ok           False                  False
  MELI           90.70               43            0.13              1.46       1556.68                57.27         0.554          pass              0.802             87.1                           0.740              -13.21             -1.323            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-05-12T10:30:01.090620-04:00 early_entry_1030 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:25:01.082139-04:00 early_entry_1025 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:20:02.261414-04:00 early_entry_1020 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:15:01.147250-04:00 early_entry_1015 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:10:05.279382-04:00 early_entry_1010 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:05:06.121865-04:00 early_entry_1005 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:00:05.800159-04:00 early_entry_1000         entry {"allocated_cash": 17500.0, "asset_type": "option", "contract_symbol": "SNPS260618C00520000", "contracts": 5, "early_entry_score": 0.854, "entry_mode": "early", "entry_option_price": 35.0, "execution_mode": "option", "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 202.0, "option_spread_pct": 0.0, "option_volume": 13.0, "success_rate": 96.97, "ticker": "SNPS", "timing_score": 0.483}
2026-05-11T12:00:16.292660-04:00 early_entry_1200 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T11:53:58.426024-04:00 early_entry_1150 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T11:47:42.065930-04:00 early_entry_1145 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260512103001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260512103001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260512103001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260512103001)

</details>
