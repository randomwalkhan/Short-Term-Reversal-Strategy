# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-02 10:05:05 EDT`
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
  CPRT     option         option CPRT261016C00032500       2026-09-01                   1    144     23760.0                 22320.0         1.65           1.55       32.33         32.39          bid_ask_mid                       1.55                bid_ask_mid                    True         -1440.0                  -6.06          87.5               16              1.99         38.72           40.48                  40.13                 398.0          105.0               0.06                      ok
```

## Today's Closed Trades (2026-09-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           83.78               37            0.84              0.73        124.57                86.77         0.616          pass              0.560             72.4                           0.719               18.78              1.603                                 ok            True                  False
   AEP           87.50               16            0.74              0.64        122.69                17.91         0.544          pass              0.407             37.7                           0.463               -3.34             -0.197                                 ok            True                  False
  PAYX          100.00               16            1.22              1.07        125.18                25.34         0.515          pass              0.630             46.1                           0.614                1.31              0.227                                 ok            True                  False
  CSCO           89.19               37            0.56              0.43        109.56                36.37         0.515          pass              0.620             47.9                           0.325               -1.28             -0.064                                 ok            True                  False
    ZS          100.00               35            1.60              1.99        177.52                60.79         0.512          pass              0.757             46.4                           0.526               -4.92              0.118                                 ok            True                  False
  MNST           84.62               13            1.44              0.45         44.80               424.41         1.000          pass              0.280             12.2                           0.241               -6.51             -0.729            downtrend_blocked_slope           False                  False
  ABNB           93.33               30            0.65              0.83        182.19                64.48         0.669          pass              0.710             51.3                           0.420               -2.70             -0.270            downtrend_blocked_slope           False                  False
   APP           72.73               44            0.30              0.66        311.46                85.96         0.651          pass              0.519             84.5                           0.775                0.00              0.210                                 ok           False                  False
   STX           87.50               32            1.01              5.76        814.17                70.47         0.602          pass              0.593             62.0                           0.370               -2.90             -0.244           downtrend_blocked_streak           False                  False
  SOXL           81.82               33            2.01              1.49        105.27                97.59         0.601          pass              0.435             57.7                           0.491              -14.05             -1.332            downtrend_blocked_slope           False                  False
  MCHP           90.24               41            0.08              0.04         71.39                59.53         0.599          pass              0.820             95.8                           0.607               -6.87             -0.606            downtrend_blocked_slope           False                  False
   WDC           78.57               28            2.21              6.96        447.46                82.26         0.585          pass              0.250             23.8                           0.306               -4.67             -0.298 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                              detail
2026-09-02T10:05:05.436409-04:00 early_entry_1005 early_entry_shadow                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T10:00:06.089036-04:00 early_entry_1000 early_entry_shadow                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T09:40:05.355091-04:00      manage_0930       exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:35:05.293548-04:00      manage_0930       exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:30:01.390795-04:00      manage_0930       exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:25:06.105664-04:00      manage_0930       exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T09:20:01.375849-04:00      manage_0930       exit_skipped {"contract_symbol": "CPRT261016C00032500", "current_ask": 0.0, "current_bid": 0.0, "current_option_price": 2.25, "current_price_source": "last_price_stale", "reason": "unreliable_option_quote", "ticker": "CPRT"}
2026-09-02T00:00:06.180126-04:00     data_refresh       data_refresh                                                                                                                                                                                                       {'saved': 93}
2026-09-01T15:10:01.952718-04:00       entry_1500       slot_skipped                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-01T15:05:02.102329-04:00       entry_1500       slot_skipped                                                                                                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260902100505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260902100505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260902100505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260902100505)

</details>
