# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-18 10:55:01 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$24,658.00`
- Equity: `$49,058.00`
- Realized PnL: `$36,898.00`
- Unrealized PnL: `$2,160.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ALNY     option         option ALNY260918C00220000       2026-08-17                   1     16     22240.0                 24400.0         13.9          15.25      224.68         227.2          bid_ask_mid                      15.25                bid_ask_mid                    True          2160.0                   9.71         84.62               26              1.73         43.62           47.31                 127.87                 332.0           21.0               0.06                      ok
```

## Today's Closed Trades (2026-08-18)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  INSM           85.00               40            0.72              0.64        128.04               109.50         0.749          pass              0.565             52.3                           0.653               29.01              1.806                      ok            True                  False
  UPRO           86.67               15            1.83              1.98        153.55                41.29         0.595          pass              0.290              6.5                           0.220               -1.66              0.000                      ok            True                  False
  NVDA           88.24               17            2.54              4.00        223.29                39.09         0.520          pass              0.340              7.4                           0.204                3.47              0.302                      ok            True                  False
  SHOP           97.62               42            0.37              0.38        148.49                85.84         0.683          pass              0.914             82.0                           0.388               20.11              1.115                      ok           False                  False
   APP           74.42               43            0.91              1.98        311.13                90.76         0.640          pass              0.345             27.0                           0.175              -26.34             -2.910 downtrend_blocked_slope           False                  False
  MSFT           82.50               40            0.07              0.25        480.24                58.97         0.630          pass              0.596             88.7                           0.479               -2.60             -0.219                      ok           False                  False
  PCAR          100.00               12            1.63              1.49        130.20                28.21         0.568          pass              0.524             18.1                           0.303               -5.08             -0.383 downtrend_blocked_slope           False                  False
  CSCO           76.47               17            1.75              1.38        112.31                42.21         0.547          pass              0.103              0.6                           0.069               -8.88             -1.028 downtrend_blocked_slope           False                  False
   HON           92.11               38            0.14              0.23        229.35                37.29         0.528          pass              0.801             79.5                           0.627               -7.63             -0.849 downtrend_blocked_slope           False                  False
  GOOG           78.72               47            0.05              0.12        341.40                46.40         0.522          pass              0.539             95.7                           0.724               -9.08             -0.831 downtrend_blocked_slope           False                  False
 GOOGL           76.09               46            0.24              0.57        343.76                47.98         0.521          pass              0.488             78.7                           0.630               -9.12             -0.814 downtrend_blocked_slope           False                  False
   CEG           78.12               32            0.69              1.35        277.20                37.62         0.506          pass              0.344             49.0                           0.314                3.22              0.580                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-18T10:55:01.557589-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T10:35:03.185404-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T10:33:08.530330-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T09:38:41.008763-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T09:20:07.104993-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T09:15:08.426968-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T09:11:00.046303-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T08:52:52.256088-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T08:35:07.917262-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T08:32:57.454440-04:00     data_refresh       data_refresh                                                         {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260818105501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260818105501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260818105501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260818105501)

</details>
