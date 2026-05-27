# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 15:10:02 EDT`
Last processed slot: `entry_1500`

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
  SNPS     option         option SNPS260717C00500000       2026-05-27                   0      2     12010.0                 11420.0        60.05           57.1       531.8        525.14          bid_ask_mid                       57.1                bid_ask_mid                    True          -590.0                  -4.91         97.22               36              0.52         54.56           56.31                  24.18                 302.0          157.0                0.1                      ok
```

## Today's Closed Trades (2026-05-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           87.10               31            1.09              2.54        331.58                92.16         0.636          pass              0.510             38.9                           0.327               11.83              1.207                                 ok            True                  False
  INTC           95.45               22            2.90              2.51        122.45                91.80         0.598          pass              0.673             44.5                           0.558               -0.56              0.404                                 ok            True                  False
  ASML           88.89               27            2.02             23.04       1622.15                54.27         0.502          pass              0.499             32.9                           0.305                5.14              0.577                                 ok            True                  False
  MSFT           86.96               23            1.04              3.04        414.73                23.55         0.501          pass              0.420             32.6                           0.302                1.18              0.209                                 ok            True                  False
  INSM           70.00               30            1.68              1.28        108.32               110.60         0.725          pass              0.311             35.1                           0.385               -7.72             -0.876            downtrend_blocked_slope           False                  False
   TRI           71.43               14            1.36              0.80         83.38                55.63         0.626          pass              0.109              6.6                           0.083               -4.66              0.164                                 ok           False                  False
   AEP           66.67               12            0.92              0.84        130.54                25.21         0.592          pass              0.132             19.7                           0.238               -1.70              0.140                                 ok           False                  False
  REGN           88.24               34            0.51              2.25        633.66                48.91         0.582          pass              0.638             66.6                           0.612              -12.59             -1.478 downtrend_blocked_slope_and_streak           False                  False
  GEHC           74.29               35            0.57              0.26         64.07                58.90         0.579          pass              0.396             57.1                           0.550                2.45              0.453                                 ok           False                  False
  PAYX           95.45               22            0.41              0.27         94.68                30.13         0.574          pass              0.675             45.8                           0.535                2.04              0.581                                 ok           False                  False
  FTNT          100.00                4            4.47              4.19        132.16                66.88         0.574          pass              0.532             24.7                           0.268               12.38              1.380                                 ok           False                  False
   ADP           94.29               35            0.44              0.68        218.06                40.06         0.530          pass              0.814             71.0                           0.496                1.67              0.492                                 ok           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527151002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527151002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527151002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527151002)

</details>
