# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-10 11:00:04 EDT`
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

- Cash: `$15,257.25`
- Equity: `$29,857.25`
- Realized PnL: `$20,222.25`
- Unrealized PnL: `$-365.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH260717C00055000       2026-06-09                   1     73     14965.0                 14600.0         2.05            2.0       52.68         52.67          bid_ask_mid                        2.0                bid_ask_mid                    True          -365.0                  -2.44         93.55               31              0.59         45.34            46.0                  51.28                1420.0           78.0                0.1                      ok
```

## Today's Closed Trades (2026-06-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MRVL          100.00               19            2.79              5.22        264.64               141.19         0.667          pass              0.666             46.3                           0.312               30.56              3.519                                 ok            True                  False
  CSCO           96.55               29            0.66              0.55        120.12                60.79         0.631          pass              0.771             60.5                           0.370               -0.08              0.150                                 ok            True                  False
    MU           80.77               26            2.01             13.17        930.24               110.66         0.626          pass              0.367             59.2                           0.363               -1.22             -0.458                                 ok            True                  False
  CTSH           90.32               31            0.62              0.23         52.84                47.83         0.566          pass              0.695             74.2                           0.552               -1.03             -0.408                                 ok            True                   True
  REGN           84.85               33            0.83              3.60        614.64                44.80         0.539          pass              0.466             43.3                           0.336               -2.66             -0.029                                 ok            True                  False
  CDNS           94.29               35            0.60              1.64        390.20                58.96         0.519          pass              0.852             84.3                           0.405                3.88              0.287                                 ok            True                  False
  VRTX           96.15               26            1.06              3.30        444.36                26.58         0.508          pass              0.649             30.4                           0.220                0.88              0.063                                 ok            True                  False
   CSX           92.86               28            0.55              0.18         47.20                21.23         0.505          pass              0.690             58.7                           0.533                0.05              0.284                                 ok            True                  False
  DRAM          100.00               17            1.27              0.53         59.63               102.89         0.718          pass              0.747             76.1                           0.432               -2.68             -0.815            downtrend_blocked_slope           False                  False
  INTU           71.43               21            2.81              5.78        291.30               101.32         0.676          pass              0.205             21.5                           0.473               -7.22             -1.172 downtrend_blocked_slope_and_streak           False                  False
   TRI           87.10               31            0.17              0.10         82.28                68.38         0.668          pass              0.680             94.8                           0.925                0.01             -0.367                                 ok           False                  False
  TEAM           92.86               42            0.39              0.26         95.50                85.52         0.607          pass              0.878             91.4                           0.767                6.93             -0.209                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-06-10T11:00:04.519159-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T10:55:01.275812-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T10:50:04.358355-04:00 early_entry_1050 early_entry_shadow                                             {"contract_symbol": "ABNB260717C00135000", "current_drop_pct": 0.54, "early_entry_score": 0.769, "early_reclaim_pct": 76.2, "entry_ask": 4.45, "entry_bid": 4.2, "entry_mode": "early", "entry_option_price": 4.325, "hypothetical_budget": 7628.63, "hypothetical_contracts": 17, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 490.0, "option_spread_pct": 5.78, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.608, "shadow_only": true, "success_rate": 91.89, "ticker": "ABNB", "timing_score": 0.431, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.769, "early_reclaim_pct": 76.2, "matched_signals": 37, "recovery_stability_score": 0.608, "success_rate": 91.89, "ticker": "ABNB", "timing_score": 0.431, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-10T10:45:02.614919-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T10:40:02.425306-04:00 early_entry_1040 early_entry_shadow                                               {"contract_symbol": "WDAY260717C00140000", "current_drop_pct": 0.61, "early_entry_score": 0.782, "early_reclaim_pct": 86.4, "entry_ask": 11.0, "entry_bid": 10.1, "entry_mode": "early", "entry_option_price": 10.55, "hypothetical_budget": 7628.63, "hypothetical_contracts": 7, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 684.0, "option_spread_pct": 8.53, "option_volume": 78.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.625, "shadow_only": true, "success_rate": 90.0, "ticker": "WDAY", "timing_score": 0.564, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.782, "early_reclaim_pct": 86.4, "matched_signals": 40, "recovery_stability_score": 0.625, "success_rate": 90.0, "ticker": "WDAY", "timing_score": 0.564, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-10T10:35:05.364684-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T10:30:02.359005-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T10:25:02.406212-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T10:20:02.419400-04:00 early_entry_1020 early_entry_shadow                   {"contract_symbol": "TEAM260717C00095000", "current_drop_pct": 1.1, "early_entry_score": 0.783, "early_reclaim_pct": 75.5, "entry_ask": 10.6, "entry_bid": 8.2, "entry_mode": "early", "entry_option_price": 9.4, "hypothetical_budget": 7628.63, "hypothetical_contracts": 8, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 25.53, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.557, "shadow_only": true, "success_rate": 91.89, "ticker": "TEAM", "timing_score": 0.592, "top_candidates": [{"current_drop_pct": 1.1, "early_entry_score": 0.783, "early_reclaim_pct": 75.5, "matched_signals": 37, "recovery_stability_score": 0.557, "success_rate": 91.89, "ticker": "TEAM", "timing_score": 0.592, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-10T10:15:01.633298-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "ABNB260724C00131000", "current_drop_pct": 0.52, "early_entry_score": 0.783, "early_reclaim_pct": 77.0, "entry_ask": 8.1, "entry_bid": 5.6, "entry_mode": "early", "entry_option_price": 6.85, "hypothetical_budget": 7628.63, "hypothetical_contracts": 11, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 36.5, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.562, "shadow_only": true, "success_rate": 92.11, "ticker": "ABNB", "timing_score": 0.425, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.783, "early_reclaim_pct": 77.0, "matched_signals": 38, "recovery_stability_score": 0.562, "success_rate": 92.11, "ticker": "ABNB", "timing_score": 0.425, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260610110004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260610110004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260610110004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260610110004)

</details>
