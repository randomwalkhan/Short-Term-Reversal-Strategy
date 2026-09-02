# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-02 10:35:02 EDT`
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
- Equity: `$47,718.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CPRT     option         option CPRT261016C00032500       2026-09-01                   1    144     23760.0                 23760.0         1.65           1.65       32.33         32.28          bid_ask_mid                       1.65                bid_ask_mid                    True             0.0                    0.0          87.5               16              1.99         38.72           40.92                  40.13                 398.0          105.0               0.06                      ok
```

## Today's Closed Trades (2026-09-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           83.33               36            1.24              1.08        124.42                86.77         0.598          pass              0.500             59.2                           0.529               18.30              1.584                                 ok            True                  False
  PAYX          100.00               13            1.47              1.29        125.09                25.34         0.519          pass              0.577             35.0                           0.298                1.06              0.215                                 ok            True                  False
    ZS          100.00               38            1.22              1.52        177.72                60.79         0.517          pass              0.816             59.2                           0.725               -4.55              0.136                                 ok            True                  False
  MNST           83.33               12            1.50              0.47         44.79               424.41         1.000          pass              0.229              8.8                           0.249               -6.57             -0.731            downtrend_blocked_slope           False                  False
  ABNB           96.43               28            0.98              1.26        182.01                64.48         0.665          pass              0.666             26.5                           0.280               -3.03             -0.285            downtrend_blocked_slope           False                  False
   APP           72.73               44            0.40              0.87        311.37                85.96         0.642          pass              0.503             79.6                           0.651               -0.09              0.205                                 ok           False                  False
   WDC           79.31               29            1.63              5.15        448.23                82.26         0.614          pass              0.319             43.6                           0.492               -4.11             -0.271 downtrend_blocked_slope_and_streak           False                  False
  MRVL           80.00               35            1.12              1.66        209.68                79.24         0.600          pass              0.424             65.7                           0.800              -12.33             -1.648 downtrend_blocked_slope_and_streak           False                  False
   STX           86.21               29            1.67              9.54        812.55                70.47         0.578          pass              0.461             37.0                           0.300               -3.55             -0.275 downtrend_blocked_slope_and_streak           False                  False
  CRWD           70.00               10            3.63              5.46        212.73                87.98         0.554          pass              0.136             26.9                           0.512                2.80              1.509                                 ok           False                  False
  AMAT           86.11               36            0.10              0.32        441.71                44.19         0.549          pass              0.675             94.6                           0.824              -10.94             -1.226 downtrend_blocked_slope_and_streak           False                  False
  FAST          100.00               17            1.14              0.39         48.58                20.15         0.523          pass              0.608             36.2                           0.461               -6.31             -0.581 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                              detail
2026-09-02T10:35:02.301132-04:00 early_entry_1035 early_entry_shadow                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:30:05.379361-04:00 early_entry_1030 early_entry_shadow                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:25:02.267090-04:00 early_entry_1025 early_entry_shadow                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:20:01.429455-04:00 early_entry_1020 early_entry_shadow                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:15:02.415633-04:00 early_entry_1015 early_entry_shadow                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:10:02.355086-04:00 early_entry_1010 early_entry_shadow                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:05:05.436409-04:00 early_entry_1005 early_entry_shadow                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:00:06.089036-04:00 early_entry_1000 early_entry_shadow                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T09:40:05.355091-04:00      manage_0930       exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:35:05.293548-04:00      manage_0930       exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260902103502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260902103502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260902103502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260902103502)

</details>
