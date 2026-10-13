# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-13 10:10:05 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$75,459.30`
- Equity: `$136,994.30`
- Realized PnL: `$123,274.30`
- Unrealized PnL: `$3,720.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261120C00290000       2026-10-12                   1     31     57815.0                 61535.0        18.65          19.85      291.07        295.22          bid_ask_mid                      19.85                bid_ask_mid                    True          3720.0                   6.43         83.33               12              2.35         48.77           48.52                  62.49                 920.0          121.0               0.05                      ok
```

## Today's Closed Trades (2026-10-13)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  CTSH     option         option CTSH261120C00060000    160          2026-10-09         2026-10-13         3.65        4.65 16000.0    27.39726 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           96.00               25            0.50              0.12         32.70                30.00         0.548          pass              0.664             36.5                           0.308                5.01              0.636                                 ok            True                  False
  INTC           85.37               41            0.55              0.39        101.18                67.41         0.565          pass              0.646             82.1                           0.790              -13.06             -1.851 downtrend_blocked_slope_and_streak           False                  False
  MPWR           88.46               26            1.19             10.96       1314.53                51.39         0.557          pass              0.554             55.3                           0.532               -3.72             -0.323            downtrend_blocked_slope           False                  False
  SNPS           87.18               39            0.39              1.35        501.93                52.43         0.542          pass              0.695             85.5                           0.640               20.59              1.537                                 ok           False                  False
  MDLZ           95.45               22            0.42              0.18         61.71                19.83         0.538          pass              0.631             32.5                           0.247                4.64              0.660                                 ok           False                  False
  REGN           83.33                6            2.27             12.13        757.61                27.51         0.516          pass              0.170              9.9                           0.121               -0.67              0.064                                 ok           False                  False
  SHOP           85.71               42            0.25              0.32        179.08                48.43         0.510          pass              0.678             91.6                           0.845               20.58              2.095                                 ok           False                  False
  UPRO           86.11               36            0.27              0.29        155.33                28.94         0.510          pass              0.555             55.8                           0.363                4.79              0.594                                 ok           False                  False
  CSCO           94.29               35            0.14              0.12        115.29                34.19         0.508          pass              0.879             93.6                           0.783                8.12              0.942                                 ok           False                  False
   XEL           86.96               23            0.43              0.22         74.07                18.13         0.508          pass              0.507             61.4                           0.358                4.47              0.567                                 ok           False                  False
   PEP           78.26               23            0.42              0.37        126.52                21.61         0.507          pass              0.201             21.3                           0.146               -1.98             -0.063                                 ok           False                  False
  ISRG           88.89                9            2.38              7.12        424.59                25.00         0.501          pass              0.289              0.8                           0.018                1.28              0.515                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-10-13T10:10:05.811238-04:00 early_entry_1010 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:05:05.477631-04:00 early_entry_1005 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:00:05.694425-04:00 early_entry_1000 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T09:50:04.590337-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "CTSH261120C00060000", "fill_price": 4.65, "pnl": 16000.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 27.4, "ticker": "CTSH"}
2026-10-13T00:00:05.318337-04:00     data_refresh       data_refresh                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-10-12T15:10:05.555878-04:00       entry_1500       slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-10-12T15:05:06.325460-04:00       entry_1500       slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-10-12T15:00:05.898503-04:00       entry_1500       slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-10-12T14:55:06.164837-04:00       entry_1500       slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-10-12T14:50:02.373216-04:00       entry_1500     timing_overlay                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-12", "training_samples": 6005, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261013101005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261013101005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261013101005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261013101005)

</details>
