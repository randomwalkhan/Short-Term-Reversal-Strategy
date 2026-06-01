# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-01 15:55:06 EDT`
Last processed slot: `manage_1600`

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
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$33,669.25`
- Equity: `$33,669.25`
- Realized PnL: `$23,669.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  MRVL     option         option MRVL260717C00200000      5          2026-06-01         2026-06-01        28.30       25.47 -1415.0       -10.0        stop_loss_hit_at_scan
  SNPS     option         option SNPS260717C00470000      4          2026-05-29         2026-06-01        35.25       42.30  2820.0        20.0 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INSM           76.19               42            0.55              0.41        106.73               110.85         0.735          pass              0.531             85.7                           0.795               -2.58             -0.134                                 ok           False                  False
   WMT           84.21               19            1.00              0.81        115.40                32.67         0.552          pass              0.369             47.3                           0.650              -12.82             -1.669 downtrend_blocked_slope_and_streak           False                  False
  LRCX           91.89               37            0.48              1.07        317.72                55.15         0.539          pass              0.810             86.3                           0.653               11.21              1.606                                 ok           False                  False
  REGN           70.00               10            2.38             10.25        610.39                42.14         0.537          pass              0.079              8.4                           0.280              -13.92             -0.871 downtrend_blocked_slope_and_streak           False                  False
   PEP           87.50                8            1.92              1.94        143.36                22.18         0.532          pass              0.264              3.5                           0.241               -5.16             -0.475            downtrend_blocked_slope           False                  False
  COST           73.33               15            1.04              6.97        953.33                27.93         0.531          pass              0.236             49.8                           0.673               -9.78             -1.322 downtrend_blocked_slope_and_streak           False                  False
  AAPL           87.50                8            1.90              4.16        310.28                17.18         0.525          pass              0.299             15.5                           0.236                1.96              0.440                                 ok           False                  False
  AMGN           66.67                3            2.19              5.16        334.58                25.52         0.521          pass              0.140             29.4                           0.534                0.95              0.247                                 ok           False                  False
  ROST           66.67                3            3.27              5.30        229.46                40.27         0.515          pass              0.082             10.1                           0.389                5.36              0.954                                 ok           False                  False
   AEP           50.00                4            2.14              1.89        125.86                24.34         0.512          pass              0.057              2.0                           0.159               -0.95             -0.078                                 ok           False                  False
   EXC           75.00                8            2.05              0.65         45.36                21.39         0.510          pass              0.081             10.1                           0.279                3.05              0.397                                 ok           False                  False
  ISRG           90.00               10            2.94              8.75        420.89                37.20         0.503          pass              0.325              2.6                           0.144               -2.13             -0.474 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                detail
2026-06-01T15:10:04.135705-04:00       entry_1500   slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-06-01T15:05:05.129733-04:00       entry_1500   slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-06-01T15:00:02.274373-04:00       entry_1500   slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-06-01T14:55:05.958850-04:00       entry_1500   slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-06-01T14:50:06.115038-04:00       entry_1500  entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T14:50:06.115038-04:00       entry_1500 timing_overlay                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-01", "training_samples": 5165, "window": 5}
2026-06-01T12:50:07.149920-04:00      manage_1300           exit {"asset_type": "option", "contract_symbol": "SNPS260717C00470000", "fill_price": 42.3, "pnl": 2820.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 20.0, "ticker": "SNPS"}
2026-06-01T12:00:03.957402-04:00 early_entry_1200  entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T11:55:05.058620-04:00 early_entry_1155  entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T11:50:02.013615-04:00 early_entry_1150  entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260601155506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260601155506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260601155506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260601155506)

</details>
