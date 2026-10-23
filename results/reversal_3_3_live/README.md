# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-23 10:15:04 EDT`
Last processed slot: `early_entry_1015`

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

- Cash: `$73,431.80`
- Equity: `$142,831.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$-2,000.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM261120C00230000       2026-10-22                   1     40     71400.0                 69400.0        17.85          17.35      223.97        222.39          bid_ask_mid                      17.35                bid_ask_mid                    True         -2000.0                   -2.8         100.0               38              0.68         80.16           82.09                  49.42                7633.0           62.0               0.11                      ok
```

## Today's Closed Trades (2026-10-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           93.33               15            1.14              0.28         35.07                27.06         0.562          pass              0.516             23.8                           0.235                9.54              0.911                                 ok            True                  False
   KHC           85.71               21            1.22              0.21         25.00                34.71         0.530          pass              0.354             25.2                           0.183               11.29              1.101                                 ok            True                  False
   MAR           85.71               14            1.30              3.62        395.25                21.06         0.530          pass              0.272             13.4                           0.215                7.04              0.931                                 ok            True                  False
   AEP           85.00               20            0.84              0.77        130.31                17.81         0.512          pass              0.255              1.4                           0.036                5.48              0.482                                 ok            True                  False
   WMT           83.33               24            0.75              0.64        120.85                23.20         0.504          pass              0.330             32.5                           0.193                7.96              0.761                                 ok            True                  False
  FAST           92.31               13            1.52              0.56         52.49                19.82         0.502          pass              0.408              3.0                           0.136                2.33              0.246                                 ok            True                  False
   CEG           85.71               28            1.09              1.94        254.38                65.49         0.605          pass              0.528             65.2                           0.665              -15.31             -1.690 downtrend_blocked_slope_and_streak           False                  False
  REGN           72.73               11            1.80             10.31        814.67                31.70         0.543          pass              0.083              7.3                           0.107                7.75              0.832                                 ok           False                  False
  TEAM          100.00               40            0.35              0.54        222.93                49.30         0.537          pass              0.881             75.6                           0.517                7.54              0.941                                 ok           False                  False
   EXC           78.57               14            1.07              0.34         44.71                20.91         0.531          pass              0.155             25.0                           0.165                6.25              0.566                                 ok           False                  False
  MDLZ           50.00                2            1.93              0.88         64.81                24.03         0.529          pass              0.103             16.6                           0.233                5.83              0.552                                 ok           False                  False
  AMGN           73.33               15            1.44              4.52        445.34                28.21         0.527          pass              0.107              6.8                           0.194                6.25              0.724                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-10-23T10:15:04.978635-04:00 early_entry_1015 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:10:06.503805-04:00 early_entry_1010 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:05:04.082507-04:00 early_entry_1005 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:00:04.565947-04:00 early_entry_1000 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T00:00:06.660227-04:00     data_refresh       data_refresh                                                                                    {'saved': 91, 'empty': 2}
2026-10-22T15:10:06.169647-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-22T15:05:02.793544-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-22T15:00:05.670192-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-22T14:55:05.642488-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-22T14:50:05.810841-04:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-22", "training_samples": 6173, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261023101504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261023101504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261023101504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261023101504)

</details>
