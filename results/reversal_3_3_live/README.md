# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-02 10:15:02 EDT`
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

- Cash: `$23,958.10`
- Equity: `$46,998.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$-720.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CPRT     option         option CPRT261016C00032500       2026-09-01                   1    144     23760.0                 23040.0         1.65            1.6       32.33         32.29          bid_ask_mid                        1.6                bid_ask_mid                    True          -720.0                  -3.03          87.5               16              1.99         38.72           39.65                  40.13                 398.0          105.0               0.06                      ok
```

## Today's Closed Trades (2026-09-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           83.78               37            0.85              0.74        124.56                86.77         0.616          pass              0.559             72.1                           0.661               18.77              1.602                                 ok            True                  False
    ZS          100.00               20            2.62              3.27        176.97                60.79         0.543          pass              0.557             12.1                           0.231               -5.91              0.071                                 ok            True                  False
  PAYX          100.00               13            1.52              1.34        125.07                25.34         0.516          pass              0.569             32.6                           0.334                1.00              0.213                                 ok            True                  False
  CSCO           89.19               37            0.68              0.53        109.51                36.37         0.507          pass              0.583             35.9                           0.291               -1.41             -0.070                                 ok            True                  False
  VRSK           85.71               14            2.38              3.23        192.96                34.83         0.503          pass              0.264             11.5                           0.173                1.76              0.329                                 ok            True                  False
  MNST           87.50               16            1.19              0.37         44.83               424.41         1.000          pass              0.423             27.7                           0.309               -6.27             -0.717            downtrend_blocked_slope           False                  False
  SOXL           82.86               35            0.66              0.49        105.70                97.59         0.671          pass              0.568             86.1                           0.826              -12.86             -1.270            downtrend_blocked_slope           False                  False
  ABNB           93.10               29            0.82              1.05        182.10                64.48         0.665          pass              0.659             38.8                           0.286               -2.86             -0.278            downtrend_blocked_slope           False                  False
   APP           72.09               43            0.47              1.03        311.30                85.96         0.646          pass              0.492             75.8                           0.665               -0.17              0.202                                 ok           False                  False
   STX           86.67               30            1.39              7.97        813.22                70.47         0.590          pass              0.512             47.4                           0.280               -3.28             -0.262 downtrend_blocked_slope_and_streak           False                  False
   WDC           78.57               28            2.21              6.98        447.45                82.26         0.584          pass              0.249             23.5                           0.217               -4.68             -0.298 downtrend_blocked_slope_and_streak           False                  False
  MRVL           79.41               34            2.08              3.06        209.08                79.24         0.547          pass              0.324             36.6                           0.552              -13.17             -1.692 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                              detail
2026-09-02T10:15:02.415633-04:00 early_entry_1015 early_entry_shadow                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:10:02.355086-04:00 early_entry_1010 early_entry_shadow                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:05:05.436409-04:00 early_entry_1005 early_entry_shadow                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:00:06.089036-04:00 early_entry_1000 early_entry_shadow                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T09:40:05.355091-04:00      manage_0930       exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:35:05.293548-04:00      manage_0930       exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:30:01.390795-04:00      manage_0930       exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:25:06.105664-04:00      manage_0930       exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:20:01.375849-04:00      manage_0930       exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T00:00:06.180126-04:00     data_refresh       data_refresh                                                                                                                                                                                                       {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260902101502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260902101502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260902101502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260902101502)

</details>
