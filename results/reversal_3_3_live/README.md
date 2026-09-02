# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-02 10:10:02 EDT`
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

- Cash: `$23,958.10`
- Equity: `$46,278.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$-1,440.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CPRT     option         option CPRT261016C00032500       2026-09-01                   1    144     23760.0                 22320.0         1.65           1.55       32.33         32.33          bid_ask_mid                       1.55                bid_ask_mid                    True         -1440.0                  -6.06          87.5               16              1.99         38.72            41.7                  40.13                 398.0          105.0               0.06                      ok
```

## Today's Closed Trades (2026-09-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           83.78               37            0.90              0.79        124.54                86.77         0.613          pass              0.553             70.4                           0.651               18.71              1.600                                 ok            True                  False
   AEP           88.24               17            0.71              0.61        122.70                17.91         0.540          pass              0.442             40.4                           0.520               -3.31             -0.195                                 ok            True                  False
  CSCO           89.19               37            0.56              0.43        109.56                36.37         0.515          pass              0.619             47.4                           0.329               -1.29             -0.064                                 ok            True                  False
    ZS          100.00               34            1.67              2.09        177.48                60.79         0.514          pass              0.743             44.0                           0.551               -4.99              0.115                                 ok            True                  False
  PAYX          100.00               15            1.40              1.24        125.11                25.34         0.510          pass              0.598             37.9                           0.427                1.12              0.218                                 ok            True                  False
  MNST           85.71               14            1.41              0.44         44.80               424.41         1.000          pass              0.322             14.2                           0.218               -6.48             -0.727            downtrend_blocked_slope           False                  False
  ABNB           96.30               27            1.04              1.33        181.98                64.48         0.667          pass              0.647             22.4                           0.250               -3.08             -0.288            downtrend_blocked_slope           False                  False
   APP           72.73               44            0.39              0.86        311.37                85.96         0.646          pass              0.504             79.7                           0.720               -0.09              0.205                                 ok           False                  False
  SOXL           82.86               35            1.14              0.85        105.55                97.59         0.643          pass              0.535             75.9                           0.573              -13.28             -1.292            downtrend_blocked_slope           False                  False
   WDC           79.31               29            1.61              5.06        448.27                82.26         0.616          pass              0.322             44.6                           0.369               -4.09             -0.270 downtrend_blocked_slope_and_streak           False                  False
   STX           88.57               35            0.51              2.93        815.38                70.47         0.615          pass              0.699             80.6                           0.435               -2.42             -0.222           downtrend_blocked_streak           False                  False
  MRVL           79.41               34            2.17              3.20        209.02                79.24         0.541          pass              0.315             33.7                           0.431              -13.25             -1.696 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                              detail
2026-09-02T10:10:02.355086-04:00 early_entry_1010 early_entry_shadow                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:05:05.436409-04:00 early_entry_1005 early_entry_shadow                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:00:06.089036-04:00 early_entry_1000 early_entry_shadow                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T09:40:05.355091-04:00      manage_0930       exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:35:05.293548-04:00      manage_0930       exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:30:01.390795-04:00      manage_0930       exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:25:06.105664-04:00      manage_0930       exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:20:01.375849-04:00      manage_0930       exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T00:00:06.180126-04:00     data_refresh       data_refresh                                                                                                                                                                                                       {'saved': 93}
2026-09-01T15:10:01.952718-04:00       entry_1500       slot_skipped                                                                                                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260902101002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260902101002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260902101002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260902101002)

</details>
