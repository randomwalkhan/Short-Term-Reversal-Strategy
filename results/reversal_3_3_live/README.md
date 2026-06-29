# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-29 15:15:05 EDT`
Last processed slot: `manual`

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

- Cash: `$14,720.50`
- Equity: `$28,720.50`
- Realized PnL: `$19,360.50`
- Unrealized PnL: `$-640.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  GILD     option         option GILD260821C00130000       2026-06-29                   0     32     14640.0                 14000.0         4.58           4.38      126.19        125.98          bid_ask_mid                       4.38                bid_ask_mid                    True          -640.0                  -4.37         93.33               15              1.32         33.41           32.67                  29.34                 807.0           40.0               0.08                      ok
```

## Today's Closed Trades (2026-06-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  DRAM           92.31               26            0.79              0.40         71.71               125.47         0.828          pass              0.786             89.5                           0.645                9.69              0.698                       ok            True                  False
   EXC           84.62               13            0.91              0.30         47.27                19.58         0.580          pass              0.262             20.4                           0.395                1.64              0.247                       ok            True                  False
  GILD           92.31               13            1.50              1.34        127.30                29.34         0.565          pass              0.464             19.7                           0.284                0.95              0.078                       ok            True                  False
  PCAR           81.82               22            1.13              0.95        120.27                36.52         0.536          pass              0.305             40.9                           0.520                0.67              0.023                       ok            True                  False
  SBUX           89.66               29            0.52              0.38        104.44                26.41         0.509          pass              0.618             60.9                           0.523                0.99              0.260                       ok            True                  False
   HON           50.00                2            4.63              7.89        240.03               250.29         0.997          pass              0.146             15.3                           0.116                5.37              5.969                       ok           False                  False
    MU           91.18               34            0.12              0.98       1131.91               130.58         0.779          pass              0.832             98.7                           0.671               15.21              1.202                       ok           False                  False
  QCOM           91.67               36            0.22              0.29        189.27                89.86         0.622          pass              0.825             92.9                           0.439              -10.74             -1.425  downtrend_blocked_slope           False                  False
   XEL          100.00               20            0.44              0.25         82.12                23.26         0.597          pass              0.679             50.8                           0.513                4.12              0.533                       ok           False                  False
  CDNS           92.59               27            1.29              3.42        375.81                56.11         0.565          pass              0.557             17.3                           0.254               -3.27             -0.557  downtrend_blocked_slope           False                  False
  CTAS           57.14                7            2.07              2.48        170.84                30.93         0.548          pass              0.057              0.7                           0.175               -4.50             -0.386  downtrend_blocked_slope           False                  False
   LIN           80.00                5            1.91              6.93        516.65                18.17         0.540          pass              0.123             22.9                           0.294               -2.65             -0.114 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-06-29T15:10:05.899695-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-29T15:05:05.773719-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-29T15:00:06.338367-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-29T14:55:08.793154-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-29T14:50:09.505108-04:00       entry_1500                   entry {"allocated_cash": 14640.0, "asset_type": "option", "contract_symbol": "GILD260821C00130000", "contracts": 32, "early_entry_score": 0.533, "entry_mode": "regular", "entry_option_price": 4.575, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 807.0, "option_spread_pct": 7.65, "option_volume": 40.0, "success_rate": 93.33, "ticker": "GILD", "timing_score": 0.563}
2026-06-29T14:50:09.505108-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                {"early_entry_score": 0.248, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 22.22, "option_volume": 0.0, "reason": "no_trade_low_option_liquidity", "ticker": "EXC", "timing_score": 0.577}
2026-06-29T14:50:09.505108-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-29", "training_samples": 5314, "window": 5}
2026-06-29T12:00:02.850105-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:55:01.636700-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:50:05.501340-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260629151505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260629151505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260629151505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260629151505)

</details>
