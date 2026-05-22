# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 10:05:01 EDT`
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
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 13210.0        30.35          33.02      415.18        414.41          bid_ask_mid                      33.02                bid_ask_mid                    True          1070.0                   8.81         91.67               36              0.62         50.17           54.84                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           81.25               32            1.36              7.25        758.99                87.43         0.632          pass              0.379             45.3                           0.343                0.66             -0.623                                 ok            True                  False
  SBUX           95.00               20            0.83              0.60        103.87                32.97         0.586          pass              0.665             46.6                           0.442               -1.01             -0.042                                 ok            True                  False
   STX           94.29               35            0.98              5.58        808.07                68.63         0.564          pass              0.676             24.1                           0.241                2.54             -0.465                                 ok            True                  False
  NVDA           85.71               21            1.57              2.41        218.48                44.83         0.533          pass              0.279              0.0                           0.157                0.40             -0.043                                 ok            True                  False
   WDC           94.29               35            1.01              3.44        484.98                59.01         0.530          pass              0.714             37.8                           0.306                0.32             -0.571                                 ok            True                  False
  CHTR           89.74               39            0.63              0.66        148.62               115.38         0.516          pass              0.667             53.9                           0.383               -4.46             -0.292                                 ok            True                  False
  INSM           78.57               42            0.36              0.27        109.41               111.27         0.751          pass              0.525             83.2                           0.447                7.69              0.092                                 ok           False                  False
   WMT           90.00               10            1.57              1.33        120.77                34.61         0.583          pass              0.339              4.5                           0.115               -8.43             -0.529            downtrend_blocked_slope           False                  False
  MSTR           90.00               40            0.69              0.80        164.51                63.46         0.553          pass              0.621             32.9                           0.267              -12.73             -1.784            downtrend_blocked_slope           False                  False
  REGN           93.33               30            0.86              3.87        640.93                49.06         0.551          pass              0.782             79.2                           0.446              -10.75             -1.532 downtrend_blocked_slope_and_streak           False                  False
  COST           71.43                7            1.52             11.17       1045.66                22.19         0.540          pass              0.080              8.5                           0.163                2.55              0.566                                 ok           False                  False
 GOOGL           87.88               33            0.70              1.90        386.85                41.05         0.535          pass              0.496             26.4                           0.257               -3.95             -0.260            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-22T10:05:01.370986-04:00 early_entry_1005  entry_skipped                                                                                   {"reason": "no_candidate"}
2026-05-22T10:00:02.359616-04:00 early_entry_1000  entry_skipped                                                                                   {"reason": "no_candidate"}
2026-05-22T00:00:04.747847-04:00     data_refresh   data_refresh                                                                                                {'saved': 92}
2026-05-21T15:10:07.725283-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-21T15:05:09.016170-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-21T15:00:06.517867-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-21T14:55:08.024423-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-21T14:50:05.768088-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-21T14:50:05.768088-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-21", "training_samples": 5058, "window": 5}
2026-05-21T12:00:02.068266-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522100501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522100501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522100501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522100501)

</details>
