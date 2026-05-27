# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 15:50:06 EDT`
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

- Cash: `$19,575.25`
- Equity: `$30,995.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$-590.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00500000       2026-05-27                   0      2     12010.0                 11420.0        60.05           57.1       531.8        528.59          bid_ask_mid                       57.1                bid_ask_mid                    True          -590.0                  -4.91         97.22               36              0.52         54.56            52.9                  24.18                 302.0          157.0                0.1                      ok
```

## Today's Closed Trades (2026-05-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           87.88               33            0.85              1.97        331.82                92.16         0.640          pass              0.585             52.6                           0.493               12.11              1.218                                 ok            True                  False
  INTC           95.65               23            2.35              2.03        122.65                91.80         0.627          pass              0.715             55.1                           0.708                0.01              0.429                                 ok            True                  False
  PAYX           95.00               20            0.52              0.34         94.65                30.13         0.580          pass              0.621             31.9                           0.374                1.93              0.576                                 ok            True                  False
  SOXL           82.61               23            3.18              5.03        223.63               148.29         0.565          pass              0.414             67.0                           0.717               26.71              2.150                                 ok            True                  False
  ASML           89.29               28            1.77             20.19       1623.38                54.27         0.513          pass              0.542             41.2                           0.502                5.41              0.588                                 ok            True                  False
  AMAT           80.77               26            1.20              3.81        453.26                55.57         0.506          pass              0.359             60.4                           0.733                4.36              0.291                                 ok            True                  False
   LIN           85.71               21            1.17              4.21        513.16                20.22         0.506          pass              0.276              0.0                           0.230                1.01              0.111                                 ok            True                  False
  INSM           69.23               26            2.30              1.75        108.12               110.60         0.712          pass              0.212             11.3                           0.137               -8.30             -0.904            downtrend_blocked_slope           False                  False
   TRI           76.92               13            1.70              1.00         83.29                55.63         0.614          pass              0.087              1.7                           0.199               -4.99              0.149                                 ok           False                  False
   AEP           72.73               11            1.03              0.94        130.50                25.21         0.599          pass              0.101             11.5                           0.298               -1.81              0.135                                 ok           False                  False
  FTNT          100.00                5            4.39              4.12        132.19                66.88         0.572          pass              0.535             26.1                           0.383               12.47              1.384                                 ok           False                  False
  REGN           87.88               33            0.76              3.37        633.18                48.91         0.571          pass              0.571             50.0                           0.324              -12.81             -1.489 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-27T15:10:02.000661-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-27T15:05:04.292282-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-27T15:00:06.354268-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-27T14:55:06.489057-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-27T14:50:01.720844-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-27T14:50:01.720844-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-27", "training_samples": 5097, "window": 5}
2026-05-27T12:00:02.710964-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-27T11:55:06.026706-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-27T11:50:03.680135-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-27T11:45:03.631384-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527155006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527155006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527155006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527155006)

</details>
