# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 10:00:02 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$16,177.75`
- Equity: `$29,387.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$1,070.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 13210.0        30.35          33.03      415.18        414.86          bid_ask_mid                      33.03                bid_ask_mid                    True          1070.0                   8.81         91.67               36              0.62         50.17           53.76                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           81.82               33            1.29              6.86        759.16                87.43         0.631          pass              0.410             48.2                           0.391                0.74             -0.620                                 ok            True                  False
  SBUX           92.86               14            1.16              0.84        103.77                32.97         0.602          pass              0.505             25.2                           0.192               -1.34             -0.057                                 ok            True                  False
   STX           94.74               38            0.65              3.66        808.89                68.63         0.566          pass              0.786             50.0                           0.296                2.89             -0.449                                 ok            True                  False
  COST           80.00               10            1.17              8.63       1046.75                22.19         0.556          pass              0.108             17.5                           0.190                2.91              0.582                                 ok            True                  False
  NVDA           89.29               28            0.96              1.47        218.88                44.83         0.536          pass              0.448              9.1                           0.081                1.03             -0.015                                 ok            True                  False
  CHTR           89.19               37            1.01              1.06        148.45               115.38         0.503          pass              0.553             26.0                           0.290               -4.82             -0.309                                 ok            True                  False
  INSM           80.85               47            0.01              0.01        109.53               111.27         0.746          pass              0.596             99.6                           0.526                8.06              0.107                                 ok           False                  False
   WMT           92.86               14            1.26              1.07        120.88                34.61         0.582          pass              0.458             10.0                           0.180               -8.14             -0.515            downtrend_blocked_slope           False                  False
  MSTR           90.00               40            0.45              0.52        164.63                63.46         0.569          pass              0.693             56.5                           0.441              -12.52             -1.773            downtrend_blocked_slope           False                  False
  REGN           94.12               34            0.54              2.44        641.54                49.06         0.546          pass              0.852             86.9                           0.545              -10.47             -1.517 downtrend_blocked_slope_and_streak           False                  False
   WDC           95.12               41            0.31              1.06        486.00                59.01         0.535          pass              0.896             80.8                           0.631                1.03             -0.539                                 ok           False                  False
 GOOGL           89.19               37            0.51              1.39        387.07                41.05         0.523          pass              0.599             40.7                           0.282               -3.77             -0.251            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-22T10:00:02.359616-04:00 early_entry_1000  entry_skipped                                                                                   {"reason": "no_candidate"}
2026-05-22T00:00:04.747847-04:00     data_refresh   data_refresh                                                                                                {'saved': 92}
2026-05-21T15:10:07.725283-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-21T15:05:09.016170-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-21T15:00:06.517867-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-21T14:55:08.024423-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-21T14:50:05.768088-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-21T14:50:05.768088-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-21", "training_samples": 5058, "window": 5}
2026-05-21T12:00:02.068266-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-21T11:55:01.035616-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522100002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522100002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522100002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522100002)

</details>
