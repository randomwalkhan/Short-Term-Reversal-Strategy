# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-28 09:35:06 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$19,575.25`
- Equity: `$31,075.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$-510.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00500000       2026-05-27                   1      2     12010.0                 11500.0        60.05           57.5       531.8        507.67     last_price_stale                        NaN                unavailable                   False          -510.0                  -4.25         97.22               36              0.52         54.56             0.0                  24.18                 302.0          157.0                0.1                      ok
```

## Today's Closed Trades (2026-05-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  ROST           92.31               26            0.96              1.57        232.80                38.54         0.562          pass              0.597             35.4                           0.288                9.19              1.209                      ok            True                  False
  AMAT           88.57               35            0.59              1.85        447.46                50.47         0.549          pass              0.611             53.5                           0.436                2.19              0.409                      ok            True                  False
  LRCX           86.21               29            1.18              2.63        317.80                56.04         0.546          pass              0.456             36.5                           0.275                6.68              1.130                      ok            True                  False
  CTSH           90.32               31            0.75              0.28         53.04                47.85         0.533          pass              0.695             75.4                           0.497               15.58              1.556                      ok            True                  False
  KLAC           85.19               27            1.28             17.55       1949.67                51.91         0.524          pass              0.320              5.4                           0.288                4.59              0.813                      ok            True                  False
  MNST           91.43               35            0.61              0.38         89.08                49.17         0.509          pass              0.692             56.5                           0.437                3.22              0.260                      ok            True                  False
  CHTR           88.89               36            0.81              0.84        146.82                56.79         0.506          pass              0.558             32.5                           0.317                2.04              0.232                      ok            True                  False
    ZS           82.35               17            2.63              2.33        125.41               152.21         0.830          pass              0.246             18.0                           0.293              -19.25             -1.255 downtrend_blocked_slope           False                  False
  INSM           77.27               44            0.18              0.13        106.34               110.67         0.767          pass              0.504             75.6                           0.613               -9.98             -0.785 downtrend_blocked_slope           False                  False
  SOXL           90.91               33            0.14              0.21        217.86               139.87         0.728          pass              0.814             98.8                           0.633               18.13              2.760                      ok           False                  False
    MU           83.78               37            0.30              1.94        927.58               100.84         0.679          pass              0.632             94.3                           0.604               15.18              2.128                      ok           False                  False
  INTU           83.87               31            1.12              2.40        306.70                90.92         0.679          pass              0.361             16.6                           0.217              -18.14             -3.018 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-28T00:00:03.757313-04:00     data_refresh   data_refresh                                                                                                {'saved': 92}
2026-05-27T15:10:02.000661-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-27T15:05:04.292282-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-27T15:00:06.354268-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-27T14:55:06.489057-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-27T14:50:01.720844-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-27T14:50:01.720844-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-27", "training_samples": 5097, "window": 5}
2026-05-27T12:00:02.710964-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-27T11:55:06.026706-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-27T11:50:03.680135-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260528093506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260528093506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260528093506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260528093506)

</details>
