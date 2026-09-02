# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-02 10:20:01 EDT`
Last processed slot: `manage_1030`

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
- Equity: `$48,438.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$720.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CPRT     option         option CPRT261016C00032500       2026-09-01                   1    144     23760.0                 24480.0         1.65            1.7       32.33         32.25          bid_ask_mid                        1.7                bid_ask_mid                    True           720.0                   3.03          87.5               16              1.99         38.72           43.31                  40.13                 398.0          105.0               0.06                      ok
```

## Today's Closed Trades (2026-09-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           83.78               37            0.91              0.80        124.54                86.77         0.612          pass              0.552             70.0                           0.657               18.70              1.599                                 ok            True                  False
  PAYX          100.00               12            1.60              1.40        125.04                25.34         0.518          pass              0.553             29.4                           0.275                0.93              0.209                                 ok            True                  False
    ZS          100.00               31            2.06              2.57        177.27                60.79         0.509          pass              0.684             31.0                           0.334               -5.36              0.097                                 ok            True                  False
  VRSK           84.62               13            2.43              3.30        192.93                34.83         0.505          pass              0.222              9.6                           0.121                1.71              0.327                                 ok            True                  False
  MNST           88.89               18            1.08              0.34         44.84               424.41         1.000          pass              0.494             34.5                           0.376               -6.17             -0.712            downtrend_blocked_slope           False                  False
  ABNB           95.45               22            1.22              1.56        181.87                64.48         0.684          pass              0.574              8.5                           0.139               -3.26             -0.296            downtrend_blocked_slope           False                  False
   APP           72.73               44            0.35              0.77        311.41                85.96         0.648          pass              0.510             81.8                           0.645               -0.05              0.207                                 ok           False                  False
   WDC           80.00               30            1.53              4.82        448.38                82.26         0.615          pass              0.337             47.2                           0.466               -4.01             -0.266 downtrend_blocked_slope_and_streak           False                  False
   STX           87.88               33            0.80              4.57        814.68                70.47         0.609          pass              0.634             69.8                           0.439               -2.70             -0.235           downtrend_blocked_streak           False                  False
  MRVL           79.41               34            1.48              2.18        209.46                79.24         0.584          pass              0.383             54.9                           0.740              -12.64             -1.664 downtrend_blocked_slope_and_streak           False                  False
  AMAT           86.11               36            0.27              0.82        441.50                44.19         0.539          pass              0.648             85.8                           0.837              -11.09             -1.233 downtrend_blocked_slope_and_streak           False                  False
  CRWD           66.67                6            4.41              6.65        212.22                87.98         0.526          pass              0.086             11.0                           0.170                1.96              1.472                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                              detail
2026-09-02T10:20:01.429455-04:00 early_entry_1020 early_entry_shadow                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:15:02.415633-04:00 early_entry_1015 early_entry_shadow                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:10:02.355086-04:00 early_entry_1010 early_entry_shadow                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:05:05.436409-04:00 early_entry_1005 early_entry_shadow                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:00:06.089036-04:00 early_entry_1000 early_entry_shadow                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T09:40:05.355091-04:00      manage_0930       exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:35:05.293548-04:00      manage_0930       exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:30:01.390795-04:00      manage_0930       exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:25:06.105664-04:00      manage_0930       exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:20:01.375849-04:00      manage_0930       exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260902102001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260902102001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260902102001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260902102001)

</details>
