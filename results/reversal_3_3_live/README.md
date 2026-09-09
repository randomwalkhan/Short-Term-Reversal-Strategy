# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-09 10:45:06 EDT`
Last processed slot: `early_entry_1045`

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
- Equity: `$77,408.10`
- Realized PnL: `$67,148.10`
- Unrealized PnL: `$260.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CRWD     option         option CRWD261016C00210000       2026-09-08                   1     26     37180.0                 37440.0         14.3           14.4      209.63        211.17          bid_ask_mid                       14.4                bid_ask_mid                    True           260.0                    0.7         88.89               36              1.63         52.75           50.84                  91.63                 699.0          116.0               0.04                      ok
```

## Today's Closed Trades (2026-09-09)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  WDAY           91.67               36            0.70              0.91        185.89                77.37         0.629          pass              0.703             52.0                           0.427               -4.86             -0.246                                 ok            True                  False
  NVDA           91.67               36            0.54              0.85        225.36                44.12         0.533          pass              0.670             44.0                           0.395                5.38              0.639                                 ok            True                  False
   CEG           86.67               15            1.35              2.84        297.84                32.90         0.518          pass              0.420             52.3                           0.371                5.96              0.767                                 ok            True                  False
  CPRT           80.77               26            1.33              0.30         32.47                44.55         0.515          pass              0.327             49.4                           0.662               -3.50             -0.082                                 ok            True                  False
  MSTR           85.37               41            0.07              0.06        136.49               103.38         0.716          pass              0.692             92.6                           0.610                7.57              0.975                                 ok           False                  False
  PYPL           94.12               34            0.34              0.13         53.13                58.35         0.601          pass              0.863             88.8                           0.692              -14.68             -1.420 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00               20            0.16              0.03         24.89                28.58         0.597          pass              0.789             87.5                           0.753               -0.25              0.076                                 ok           False                  False
  AMGN           97.22               36            0.01              0.03        393.16                44.47         0.573          pass              0.928             99.0                           0.598              -11.10             -0.870 downtrend_blocked_slope_and_streak           False                  False
   PEP          100.00                7            1.22              1.18        137.94                16.46         0.573          pass              0.471              4.5                           0.122               -2.85             -0.214                                 ok           False                  False
  PAYX          100.00               16            1.20              0.98        116.51                30.90         0.570          pass              0.572             25.0                           0.289               -7.57             -0.754            downtrend_blocked_slope           False                  False
  PANW           86.96               46            0.22              0.53        336.75                67.50         0.562          pass              0.690             82.8                           0.648               -1.08             -0.795                                 ok           False                  False
  ADBE           94.74               38            0.10              0.17        257.19                50.01         0.560          pass              0.876             80.0                           0.536               -6.17             -0.812            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-09-09T10:45:06.010738-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:40:05.945094-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "WDAY261016C00185000", "current_drop_pct": 0.52, "early_entry_score": 0.754, "early_reclaim_pct": 64.6, "entry_ask": 12.6, "entry_bid": 10.5, "entry_mode": "early", "entry_option_price": 11.55, "hypothetical_budget": 19984.05, "hypothetical_contracts": 17, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 118.0, "option_spread_pct": 18.18, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.559, "shadow_only": true, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.634, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.754, "early_reclaim_pct": 64.6, "matched_signals": 37, "recovery_stability_score": 0.559, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.634, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-09T10:35:01.934263-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:30:01.975692-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:25:04.909615-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:20:01.984247-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:15:03.852683-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:10:05.084916-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:05:03.958272-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:00:05.981446-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260909104506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260909104506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260909104506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260909104506)

</details>
