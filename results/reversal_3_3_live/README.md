# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-17 09:35:02 EST`
Last processed slot: `manage_0930`

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

- Cash: `$59,174.80`
- Equity: `$113,878.80`
- Realized PnL: `$107,024.80`
- Unrealized PnL: `$-3,146.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  QCOM     option         option QCOM261218C00170000       2026-11-16                   1     52     57850.0                 54704.0        11.12          10.52      170.26        167.51     last_price_stale                        NaN                unavailable                   False         -3146.0                  -5.44         85.19               27              1.28         54.03            1.56                  68.34                3371.0          163.0               0.02                      ok
```

## Today's Closed Trades (2026-11-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   AEP          100.00               11            0.58              0.52        129.12                17.11         0.597          pass              0.551             28.4                           0.567               -0.22              0.153                                 ok            True                  False
  QCOM           89.47               38            0.58              0.68        168.23                68.75         0.590          pass              0.700             67.1                           0.430                1.90              0.398                                 ok            True                  False
  VRSK           80.00               20            1.60              2.38        211.74                44.55         0.573          pass              0.231             35.6                           0.498                6.27              0.533                                 ok            True                  False
  INSM           84.09               44            0.61              0.53        122.65                61.88         0.563          pass              0.527             54.0                           0.371               16.94              1.501                                 ok            True                  False
   ADP           86.36               22            1.08              2.37        312.41                28.40         0.543          pass              0.378             24.7                           0.173                4.74              0.392                                 ok            True                  False
  META           81.82               33            0.63              2.74        625.23                41.97         0.529          pass              0.415             53.4                           0.453                0.24              0.172                                 ok            True                  False
   EXC           88.89               27            0.63              0.21         46.37                21.89         0.519          pass              0.472             23.4                           0.203                1.46              0.066                                 ok            True                  False
  INTC           67.86               28            2.19              0.85         55.08               143.34         0.813          pass              0.338             45.7                           0.355              -10.44             -0.119           downtrend_blocked_streak           False                  False
   APP           91.84               49            0.40              1.17        414.72               119.50         0.784          pass              0.805             70.3                           0.678               68.45              4.290                                 ok           False                  False
  DRAM           65.52               29            1.22              0.34         39.15               109.09         0.743          pass              0.306             35.0                           0.262              -18.54             -0.809 downtrend_blocked_slope_and_streak           False                  False
    MU           69.70               33            0.91              4.56        717.07               106.43         0.723          pass              0.393             55.9                           0.321              -16.68             -0.373 downtrend_blocked_slope_and_streak           False                  False
  KLAC           74.29               35            0.53              0.54        143.73                90.70         0.687          pass              0.319             28.0                           0.280               -8.19              0.197           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-11-17T00:00:04.730535-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                {'saved': 91, 'empty': 2}
2026-11-16T15:10:06.484281-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-16T15:05:04.471128-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-16T15:00:02.614277-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-16T14:55:05.526400-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-16T14:50:05.632368-05:00       entry_1500              entry {"allocated_cash": 57850.0, "asset_type": "option", "contract_symbol": "QCOM261218C00170000", "contracts": 52, "early_entry_score": 0.463, "entry_mode": "regular", "entry_option_price": 11.125, "execution_mode": "option", "matched_signals": 27, "option_liquidity_status": "ok", "option_open_interest": 3371.0, "option_spread_pct": 2.25, "option_volume": 163.0, "success_rate": 85.19, "ticker": "QCOM", "timing_score": 0.599}
2026-11-16T14:50:05.632368-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                             {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-16", "training_samples": 6252, "window": 5}
2026-11-16T12:00:06.189973-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:55:04.372932-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:50:05.541562-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261117093502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261117093502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261117093502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261117093502)

</details>
