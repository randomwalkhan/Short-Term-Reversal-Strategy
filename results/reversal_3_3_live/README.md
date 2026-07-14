# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-14 10:50:01 EDT`
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

- Cash: `$17,620.25`
- Equity: `$26,560.25`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$-435.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  META     option         option META260821C00660000       2026-07-13                   1      2      9375.0                  8940.0        46.88           44.7      660.72        660.71          bid_ask_mid                       44.7                bid_ask_mid                    True          -435.0                  -4.64         81.82               22              1.27         53.38           51.44                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   PEP           90.00               10            1.06              1.03        138.05                30.22         0.626          pass              0.408             26.1                           0.241               -1.20             -0.104                  ok            True                  False
  AAPL           95.45               22            0.92              2.05        316.43                35.57         0.587          pass              0.706             55.8                           0.642               11.58              1.111                  ok            True                  False
  PYPL           80.00               10            1.89              0.63         47.38                33.27         0.562          pass              0.135             26.2                           0.260                5.34              0.634                  ok            True                  False
  GILD           86.36               22            0.82              0.75        131.08                32.97         0.558          pass              0.443             45.7                           0.408                3.16              0.415                  ok            True                  False
  QCOM           82.76               29            1.16              1.50        183.34                63.33         0.555          pass              0.426             56.9                           0.572               -3.64              0.132                  ok            True                  False
  TMUS           88.00               25            1.00              1.32        187.85                37.13         0.551          pass              0.413             14.7                           0.144                7.22              1.013                  ok            True                  False
  PAYX          100.00               26            0.79              0.62        110.49                31.82         0.539          pass              0.798             79.3                           0.698               10.08              0.955                  ok            True                  False
  PCAR           83.33               24            1.05              0.92        123.87                31.62         0.536          pass              0.256              6.8                           0.075                2.80              0.393                  ok            True                  False
  CTAS           88.00               25            0.96              1.23        183.22                31.28         0.531          pass              0.507             46.8                           0.453                7.64              0.647                  ok            True                  False
  AMGN           95.65               23            0.96              2.43        359.41                21.45         0.522          pass              0.654             38.4                           0.489               -0.99             -0.079                  ok            True                  False
  IDXX           90.00               10            2.76             10.91        559.54                34.15         0.516          pass              0.385             22.2                           0.275                2.37              0.504                  ok            True                  False
  CSCO           96.67               30            0.86              0.72        118.94                35.64         0.512          pass              0.585              0.0                           0.263                0.82              0.275                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-07-14T10:50:01.398804-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "DASH260814C00190000", "current_drop_pct": 0.5, "early_entry_score": 0.889, "early_reclaim_pct": 81.1, "entry_ask": 13.75, "entry_bid": 11.3, "entry_mode": "early", "entry_option_price": 12.525, "hypothetical_budget": 8810.13, "hypothetical_contracts": 7, "matched_signals": 45, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 14.0, "option_spread_pct": 19.56, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.826, "shadow_only": true, "success_rate": 95.56, "ticker": "DASH", "timing_score": 0.459, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.889, "early_reclaim_pct": 81.1, "matched_signals": 45, "recovery_stability_score": 0.826, "success_rate": 95.56, "ticker": "DASH", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-14T10:45:05.382640-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:40:02.394699-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:35:01.379704-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:30:01.227428-04:00 early_entry_1030 early_entry_shadow                 {"contract_symbol": "DASH260821C00190000", "current_drop_pct": 0.64, "early_entry_score": 0.873, "early_reclaim_pct": 75.7, "entry_ask": 14.35, "entry_bid": 11.7, "entry_mode": "early", "entry_option_price": 13.025, "hypothetical_budget": 8810.13, "hypothetical_contracts": 6, "matched_signals": 44, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 268.0, "option_spread_pct": 20.35, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.693, "shadow_only": true, "success_rate": 95.45, "ticker": "DASH", "timing_score": 0.457, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.873, "early_reclaim_pct": 75.7, "matched_signals": 44, "recovery_stability_score": 0.693, "success_rate": 95.45, "ticker": "DASH", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-14T10:25:01.405128-04:00 early_entry_1025 early_entry_shadow    {"contract_symbol": "VRSK260821C00190000", "current_drop_pct": 0.63, "early_entry_score": 0.711, "early_reclaim_pct": 79.9, "entry_ask": 12.0, "entry_bid": 9.5, "entry_mode": "early", "entry_option_price": 10.75, "hypothetical_budget": 8810.13, "hypothetical_contracts": 8, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 23.26, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.655, "shadow_only": true, "success_rate": 89.19, "ticker": "VRSK", "timing_score": 0.465, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.711, "early_reclaim_pct": 79.9, "matched_signals": 37, "recovery_stability_score": 0.655, "success_rate": 89.19, "ticker": "VRSK", "timing_score": 0.465, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-14T10:20:04.363539-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:15:01.411533-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:10:01.422460-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:05:01.368977-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260714105001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260714105001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260714105001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260714105001)

</details>
