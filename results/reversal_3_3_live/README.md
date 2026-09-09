# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-09 11:05:02 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$39,968.10`
- Equity: `$77,993.10`
- Realized PnL: `$67,148.10`
- Unrealized PnL: `$845.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CRWD     option         option CRWD261016C00210000       2026-09-08                   1     26     37180.0                 38025.0         14.3          14.62      209.63        208.97          bid_ask_mid                      14.62                bid_ask_mid                    True           845.0                   2.27         88.89               36              1.63         52.75           56.18                  91.63                 699.0          116.0               0.04                      ok
```

## Today's Closed Trades (2026-09-09)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           83.78               37            0.95              0.91        136.13               103.38         0.685          pass              0.440             30.3                           0.267                6.62              0.935                                 ok            True                  False
   KHC          100.00               11            0.70              0.12         24.85                28.58         0.618          pass              0.604             45.3                           0.300               -0.79              0.051                                 ok            True                  False
   EXC          100.00               12            0.68              0.21         43.86                15.52         0.566          pass              0.516             15.5                           0.216               -0.55              0.005                                 ok            True                  False
   AEP           87.50               16            0.77              0.67        125.13                16.51         0.538          pass              0.306              4.0                           0.179                1.38              0.206                                 ok            True                  False
  NVDA           91.67               36            0.58              0.92        225.34                44.12         0.531          pass              0.657             39.9                           0.326                5.34              0.637                                 ok            True                  False
  CPRT           86.36               22            1.73              0.40         32.43                44.55         0.522          pass              0.405             34.3                           0.349               -3.89             -0.100                                 ok            True                  False
   CEG           85.71               14            1.69              3.55        297.53                32.90         0.503          pass              0.350             40.3                           0.225                5.59              0.751                                 ok            True                  False
   XEL           85.71               14            1.47              0.79         76.54                17.22         0.501          pass              0.244              5.0                           0.173               -1.87             -0.179                                 ok            True                  False
  CRWD           91.30               46            0.36              0.54        209.79                89.86         0.657          pass              0.735             55.8                           0.339               12.88              0.602                                 ok           False                  False
  PYPL           95.45               22            1.02              0.38         53.02                58.35         0.632          pass              0.742             66.2                           0.363              -15.26             -1.451 downtrend_blocked_slope_and_streak           False                  False
  WDAY           91.43               35            0.82              1.07        185.82                77.37         0.627          pass              0.665             43.7                           0.352               -4.97             -0.252            downtrend_blocked_slope           False                  False
  AMGN           96.88               32            0.21              0.59        392.92                44.47         0.585          pass              0.841             78.5                           0.448              -11.29             -0.879 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-09-09T11:05:02.949685-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T11:00:04.107755-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:55:03.946736-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:50:02.088506-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:45:06.010738-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:40:05.945094-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "WDAY261016C00185000", "current_drop_pct": 0.52, "early_entry_score": 0.754, "early_reclaim_pct": 64.6, "entry_ask": 12.6, "entry_bid": 10.5, "entry_mode": "early", "entry_option_price": 11.55, "hypothetical_budget": 19984.05, "hypothetical_contracts": 17, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 118.0, "option_spread_pct": 18.18, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.559, "shadow_only": true, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.634, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.754, "early_reclaim_pct": 64.6, "matched_signals": 37, "recovery_stability_score": 0.559, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.634, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-09T10:35:01.934263-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:30:01.975692-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:25:04.909615-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:20:01.984247-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260909110502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260909110502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260909110502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260909110502)

</details>
