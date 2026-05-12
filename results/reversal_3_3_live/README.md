# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-12 10:55:01 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$33,603.50`
- Equity: `$33,603.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-12)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SNPS     option         option SNPS260618C00520000      5          2026-05-12         2026-05-12         35.0        31.5 -1750.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           91.67               12            1.85              3.86        296.11                67.69         0.709          pass              0.500             35.0                           0.532               10.84              0.976                                 ok            True                  False
  TEAM           86.84               38            1.25              0.76         86.98               115.89         0.703          pass              0.589             50.0                           0.388               23.68              2.549                                 ok            True                  False
  GOOG           88.89               36            0.63              1.69        386.04                39.86         0.545          pass              0.610             48.4                           0.565               10.60              1.051                                 ok            True                  False
    ZS           83.33               36            0.89              0.92        148.47                59.15         0.535          pass              0.469             51.1                           0.519                8.44              1.280                                 ok            True                  False
   XEL           93.75               16            1.09              0.62         80.34                27.14         0.531          pass              0.656             65.4                           0.460                0.30             -0.077                                 ok            True                  False
  CDNS           96.30               27            1.50              3.84        362.56                37.36         0.525          pass              0.634             22.6                           0.309               10.27              1.160                                 ok            True                  False
   CSX           84.62               26            0.96              0.30         44.61                30.07         0.519          pass              0.331             16.5                           0.343               -2.03             -0.133                                 ok            True                  False
  MNST           86.11               36            0.54              0.33         86.27                49.64         0.515          pass              0.638             83.5                           0.696               11.34              1.211                                 ok            True                  False
  CHTR           89.58               48            0.18              0.19        147.71               118.46         0.773          pass              0.788             84.9                           0.429              -14.78             -1.352            downtrend_blocked_slope           False                  False
 CMCSA           95.24               21            0.74              0.13         24.97                62.25         0.705          pass              0.602             19.6                           0.219              -10.11             -0.994 downtrend_blocked_slope_and_streak           False                  False
  SHOP           90.24               41            0.59              0.42        102.36                84.99         0.657          pass              0.696             52.5                           0.315              -16.48             -2.096            downtrend_blocked_slope           False                  False
  NXPI           66.67               12            3.30              7.07        302.96                87.21         0.619          pass              0.249             58.1                           0.373               28.43              1.342                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                           detail
2026-05-12T10:55:01.118172-04:00 early_entry_1055 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:50:05.198846-04:00 early_entry_1050 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:45:04.189034-04:00 early_entry_1045 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:40:01.090615-04:00 early_entry_1040 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:35:01.096348-04:00 early_entry_1035 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:35:01.096348-04:00      manage_1030          exit {"asset_type": "option", "contract_symbol": "SNPS260618C00520000", "fill_price": 31.5, "pnl": -1750.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SNPS"}
2026-05-12T10:30:01.090620-04:00 early_entry_1030 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:25:01.082139-04:00 early_entry_1025 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:20:02.261414-04:00 early_entry_1020 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:15:01.147250-04:00 early_entry_1015 entry_skipped                                                                                                                                                  {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260512105501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260512105501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260512105501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260512105501)

</details>
