# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-15 10:20:02 EDT`
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

- Cash: `$19,710.25`
- Equity: `$28,450.25`
- Realized PnL: `$19,085.25`
- Unrealized PnL: `$-635.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  META     option         option META260821C00660000       2026-07-13                   2      2      9375.0                  8740.0        46.88           43.7      660.72        668.16          bid_ask_mid                       43.7                bid_ask_mid                    True          -635.0                  -6.77         81.82               22              1.27         53.38           46.16                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AAPL     option         option AAPL260821C00315000     11          2026-07-14         2026-07-15        11.55       13.45 2090.0   16.450216 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MPWR           81.25               32            1.01              9.69       1372.26                84.79         0.657          pass              0.258              4.1                           0.196               -1.43              0.187                                 ok            True                  False
  MCHP           90.91               33            0.85              0.52         86.89                68.63         0.611          pass              0.505              0.0                           0.251               -5.30             -0.233                                 ok            True                  False
   EXC           93.33               15            0.77              0.25         46.81                21.56         0.568          pass              0.559             37.9                           0.321               -0.13             -0.053                                 ok            True                  False
   AEP           83.33               12            1.29              1.22        134.42                21.64         0.562          pass              0.195             12.1                           0.115               -2.64             -0.214                                 ok            True                  False
   LIN          100.00               12            1.25              4.57        520.58                20.66         0.560          pass              0.540             23.6                           0.269               -0.56             -0.301                                 ok            True                  False
   CSX           86.67               15            0.99              0.35         49.77                19.08         0.559          pass              0.361             31.2                           0.321                3.99              0.350                                 ok            True                  False
   WBD           87.50               16            0.80              0.15         27.41                20.00         0.536          pass              0.387             31.3                           0.314                2.25              0.282                                 ok            True                  False
  SOXL           85.71               21            5.45              6.74        173.77               219.49         0.793          pass              0.313              2.7                           0.198              -37.37             -3.008            downtrend_blocked_slope           False                  False
  AMAT           85.00               20            2.20              9.17        591.77                98.89         0.657          pass              0.276              3.4                           0.137              -19.42             -1.352 downtrend_blocked_slope_and_streak           False                  False
  KLAC           80.00               20            3.13              5.05        228.20               109.33         0.641          pass              0.131              0.0                           0.183              -26.04             -2.053 downtrend_blocked_slope_and_streak           False                  False
   TXN           91.67               36            0.29              0.61        305.29                65.52         0.615          pass              0.781             78.4                           0.514                2.22              0.335                                 ok           False                  False
   ADI           88.57               35            0.34              0.95        392.34                55.85         0.600          pass              0.526             23.7                           0.256               -1.45              0.118                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                  detail
2026-07-15T10:20:02.772383-04:00 early_entry_1020 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:15:05.965611-04:00 early_entry_1015 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:10:03.001163-04:00 early_entry_1010 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:05:02.748975-04:00 early_entry_1005 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:00:03.493578-04:00 early_entry_1000 early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T10:00:03.493578-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "AAPL260821C00315000", "fill_price": 13.45, "pnl": 2090.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.45, "ticker": "AAPL"}
2026-07-15T09:35:02.740173-04:00     data_refresh       data_refresh                                                                                                                                                                           {'saved': 93}
2026-07-15T09:30:04.740888-04:00     data_refresh       data_refresh                                                                                                                                                                           {'saved': 93}
2026-07-15T09:25:03.806265-04:00     data_refresh       data_refresh                                                                                                                                                                           {'saved': 93}
2026-07-15T09:20:04.874058-04:00     data_refresh       data_refresh                                                                                                                                                                           {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260715102002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260715102002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260715102002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260715102002)

</details>
