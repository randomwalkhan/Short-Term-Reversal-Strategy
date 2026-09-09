# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-09 11:15:03 EDT`
Last processed slot: `early_entry_1115`

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
- Equity: `$76,953.10`
- Realized PnL: `$67,148.10`
- Unrealized PnL: `$-195.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CRWD     option         option CRWD261016C00210000       2026-09-08                   1     26     37180.0                 36985.0         14.3          14.22      209.63        208.99          bid_ask_mid                      14.22                bid_ask_mid                    True          -195.0                  -0.52         88.89               36              1.63         52.75           54.65                  91.63                 699.0          116.0               0.04                      ok
```

## Today's Closed Trades (2026-09-09)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           80.65               31            1.61              1.54        135.86               103.38         0.675            pass              0.278             17.8                           0.215                5.91              0.905                                 ok            True                  False
  CRWD           91.11               45            0.56              0.82        209.67                89.86         0.652            pass              0.659             32.4                           0.184               12.66              0.594                                 ok            True                  False
   KHC          100.00               12            0.60              0.10         24.86                28.58         0.618            pass              0.635             53.1                           0.307               -0.69              0.056                                 ok            True                  False
   EXC          100.00               12            0.68              0.21         43.86                15.52         0.566            pass              0.516             15.5                           0.167               -0.55              0.005                                 ok            True                  False
  NVDA           91.67               36            0.56              0.88        225.35                44.12         0.532            pass              0.664             42.2                           0.370                5.36              0.638                                 ok            True                  False
   AEP           88.89               18            0.68              0.60        125.16                16.51         0.531            pass              0.412             22.7                           0.219                1.46              0.209                                 ok            True                  False
  CPRT           86.36               22            1.70              0.39         32.43                44.55         0.524            pass              0.408             35.5                           0.286               -3.86             -0.099                                 ok            True                  False
  UPRO           87.50               16            1.69              1.76        148.54                24.94         0.506            pass              0.311              6.6                           0.250               -2.11             -0.115                                 ok            True                  False
   XEL           86.67               15            1.39              0.75         76.56                17.22         0.500 below_threshold              0.311             16.8                           0.204               -1.78             -0.176                                 ok            True                  False
  PYPL           95.83               24            0.86              0.32         53.04                58.35         0.630            pass              0.770             71.4                           0.359              -15.12             -1.444 downtrend_blocked_slope_and_streak           False                  False
  WDAY           91.43               35            0.96              1.25        185.75                77.37         0.619            pass              0.636             34.3                           0.243               -5.10             -0.258            downtrend_blocked_slope           False                  False
  AMGN           97.14               35            0.04              0.10        393.13                44.47         0.578            pass              0.914             96.4                           0.540              -11.13             -0.871 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-09-09T11:15:03.937186-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T11:10:03.934415-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T11:05:02.949685-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T11:00:04.107755-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:55:03.946736-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:50:02.088506-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:45:06.010738-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:40:05.945094-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "WDAY261016C00185000", "current_drop_pct": 0.52, "early_entry_score": 0.754, "early_reclaim_pct": 64.6, "entry_ask": 12.6, "entry_bid": 10.5, "entry_mode": "early", "entry_option_price": 11.55, "hypothetical_budget": 19984.05, "hypothetical_contracts": 17, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 118.0, "option_spread_pct": 18.18, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.559, "shadow_only": true, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.634, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.754, "early_reclaim_pct": 64.6, "matched_signals": 37, "recovery_stability_score": 0.559, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.634, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-09T10:35:01.934263-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:30:01.975692-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260909111503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260909111503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260909111503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260909111503)

</details>
