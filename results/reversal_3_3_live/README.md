# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-01 16:00:08 EDT`
Last processed slot: `manage_1600`

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

- Cash: `$27,896.50`
- Equity: `$27,896.50`
- Realized PnL: `$17,896.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  GILD     option         option GILD260821C00130000     32          2026-06-29         2026-07-01        4.575      4.1175 -1464.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   XEL          100.00               18            0.74              0.42         80.12                19.51         0.576          pass              0.629             39.3                           0.620                0.92              0.422                                 ok            True                  False
   AEP           81.82               11            1.26              1.20        136.29                19.16         0.556          pass              0.190             26.5                           0.436                4.12              0.764                                 ok            True                  False
  AVGO           76.47               17            2.15              5.67        375.32                74.76         0.673          pass              0.164             16.6                           0.209               -1.72             -0.616            downtrend_blocked_slope           False                  False
  MCHP           92.86               14            2.75              1.76         90.45                74.43         0.632          pass              0.441              2.7                           0.225               -7.26             -1.041            downtrend_blocked_slope           False                  False
   ADI           87.50               16            2.12              5.89        394.65                64.06         0.622          pass              0.337             11.7                           0.155               -6.55             -0.977            downtrend_blocked_slope           False                  False
  NXPI           90.62               32            0.65              1.28        280.48                65.46         0.611          pass              0.742             83.6                           0.485               -7.51             -1.146            downtrend_blocked_slope           False                  False
  QCOM           82.61               23            1.60              2.06        183.91                83.64         0.609          pass              0.311             31.2                           0.218              -15.06             -2.035 downtrend_blocked_slope_and_streak           False                  False
  UPRO           88.24               34            0.28              0.28        141.67                55.16         0.602          pass              0.687             82.5                           0.368               -1.69             -0.185                                 ok           False                  False
  MPWR           84.21               19            3.61             34.94       1367.39                91.02         0.583          pass              0.252              7.0                           0.213              -11.10             -1.459            downtrend_blocked_slope           False                  False
   EXC           78.57               14            0.79              0.26         46.51                18.60         0.579          pass              0.183             32.7                           0.425               -0.73              0.188                                 ok           False                  False
  ROST           93.75               32            0.43              0.64        212.57                34.96         0.524          pass              0.764             66.0                           0.606               -9.62             -1.338 downtrend_blocked_slope_and_streak           False                  False
   WDC          100.00                9            6.33             28.29        626.59               116.88         0.514          pass              0.522             23.6                           0.299              -12.15             -1.752            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et        slot              event_type                                                                                                                                                                                                                                                                 detail
2026-07-01T15:20:08.894033-04:00 manage_1530                    exit                                                                                     {"asset_type": "option", "contract_symbol": "GILD260821C00130000", "fill_price": 4.1175, "pnl": -1464.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "GILD"}
2026-07-01T15:10:11.143271-04:00  entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T15:05:07.919397-04:00  entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T15:00:09.367331-04:00  entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T14:55:05.861766-04:00  entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T14:50:09.429141-04:00  entry_1500           entry_skipped                                                                                                                                                                                                                 {"reason": "no_trade_after_option_and_timing_filters"}
2026-07-01T14:50:09.429141-04:00  entry_1500 entry_candidate_skipped                    {"early_entry_score": 0.2, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 720.0, "option_spread_pct": 17.39, "option_volume": 4.0, "reason": "no_trade_low_option_liquidity", "ticker": "AEP", "timing_score": 0.543}
2026-07-01T14:50:09.429141-04:00  entry_1500 entry_candidate_skipped                           {"early_entry_score": 0.643, "option_liquidity_status": "wide_spread", "option_open_interest": 1263.0, "option_spread_pct": 16.22, "option_volume": 24.0, "reason": "no_trade_low_option_liquidity", "ticker": "XEL", "timing_score": 0.571}
2026-07-01T14:50:09.429141-04:00  entry_1500 entry_candidate_skipped {"early_entry_score": 0.275, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 12.0, "option_spread_pct": 31.25, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "EXC", "timing_score": 0.587}
2026-07-01T14:50:09.429141-04:00  entry_1500          timing_overlay                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-01", "training_samples": 5334, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260701160008)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260701160008)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260701160008)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260701160008)

</details>
