# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-31 15:05:50 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$167.25`
- Equity: `$34,297.25`
- Realized PnL: `$23,222.25`
- Unrealized PnL: `$1,075.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option  CSX260918C00050000       2026-07-30                   1     86     16555.0                 17630.0         1.92           2.05       50.11         50.44          bid_ask_mid                       2.05                bid_ask_mid                    True          1075.0                   6.49         92.31               13              1.24         25.34           24.51                  28.82                2759.0          136.0               0.03                      ok
  PYPL     option         option PYPL260918C00057500       2026-07-31                   0     66     16500.0                 16500.0         2.50           2.50       57.10         57.10          bid_ask_mid                       2.50                bid_ask_mid                    True             0.0                   0.00         86.21               29              0.95         31.54           31.54                  60.55                6425.0          263.0               0.05                      ok
```

## Today's Closed Trades (2026-07-31)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PYPL           86.21               29            0.95              0.38         57.49                60.55         0.642          pass              0.505             49.5                           0.416                0.96              0.307                                 ok            True                  False
  MDLZ          100.00               12            1.29              0.57         62.84                34.51         0.600          pass              0.563             29.7                           0.236                2.07              0.540                                 ok            True                  False
   KHC           91.67               12            1.55              0.29         26.26                32.41         0.578          pass              0.459             25.5                           0.286                0.35              0.397                                 ok            True                  False
  CTAS           92.59               27            0.84              1.21        206.27                40.09         0.568          pass              0.685             59.8                           0.468                0.30              0.466                                 ok            True                  False
  MNST           88.89               18            1.02              0.70         97.35                23.72         0.540          pass              0.425             27.0                           0.409               -0.87              0.178                                 ok            True                  False
  GILD           85.71               28            0.61              0.56        131.04                35.61         0.538          pass              0.552             75.4                           0.580               -2.83             -0.080                                 ok            True                  False
   TRI           85.71               42            0.56              0.39         98.66                65.88         0.513          pass              0.650             82.0                           0.792                2.16              1.083                                 ok            True                  False
  ALNY           90.70               43            0.48              0.70        205.18               124.46         0.740          pass              0.804             81.5                           0.741              -23.55             -1.928            downtrend_blocked_slope           False                  False
  TMUS           92.31               26            0.89              1.09        172.87                56.67         0.618          pass              0.670             57.7                           0.653              -10.73             -1.139            downtrend_blocked_slope           False                  False
  DRAM           79.31               29            2.23              0.82         51.99               113.92         0.579          pass              0.317             44.0                           0.358               -2.93             -1.368 downtrend_blocked_slope_and_streak           False                  False
  GEHC           88.89                9            2.49              1.22         69.42                56.76         0.578          pass              0.407             37.4                           0.511                8.19              1.221                                 ok           False                  False
   KDP           76.47               17            1.38              0.30         31.44                32.85         0.543          pass              0.209             36.0                           0.342                0.73              0.341                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-07-31T15:05:50.400930-04:00       entry_1500              entry {"allocated_cash": 16500.0, "asset_type": "option", "contract_symbol": "PYPL260918C00057500", "contracts": 66, "early_entry_score": 0.505, "entry_mode": "regular", "entry_option_price": 2.5, "execution_mode": "option", "matched_signals": 29, "option_liquidity_status": "ok", "option_open_interest": 6425.0, "option_spread_pct": 4.8, "option_volume": 263.0, "success_rate": 86.21, "ticker": "PYPL", "timing_score": 0.642}
2026-07-31T15:05:50.400930-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-31", "training_samples": 5549, "window": 5}
2026-07-31T11:24:55.037257-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-31T11:01:50.323934-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-31T10:17:02.389266-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-31T00:00:05.700754-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 93}
2026-07-30T15:10:05.973012-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-30T15:05:01.482451-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-30T15:00:04.923980-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-30T14:55:06.025633-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260731150550)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260731150550)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260731150550)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260731150550)

</details>
