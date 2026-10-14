# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-14 10:35:03 EDT`
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

- Cash: `$135,462.30`
- Equity: `$135,462.30`
- Realized PnL: `$125,462.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-14)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SNPS     option         option SNPS261120C00500000     28          2026-10-13         2026-10-14         25.4       22.86 -7112.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  UPRO          100.00               10            1.96              2.13        154.49                28.27         0.551          pass              0.480              8.4                           0.208                3.67              0.431                                 ok            True                  False
   XEL           86.36               22            0.51              0.27         74.53                17.32         0.526          pass              0.337             11.6                           0.184                5.36              0.611                                 ok            True                  False
  SHOP           85.00               40            0.50              0.62        176.25                46.81         0.510          pass              0.571             62.3                           0.282               18.43              1.962                                 ok            True                  False
    ZS           90.91               33            1.44              2.30        227.67                58.33         0.508          pass              0.657             54.1                           0.551               13.01              1.729                                 ok            True                  False
  MSFT           96.15               26            0.68              2.57        542.35                20.68         0.502          pass              0.611             18.2                           0.231                5.24              0.587                                 ok            True                  False
   EXC           85.00               20            0.74              0.22         42.25                15.81         0.501          pass              0.295             14.9                           0.193                4.02              0.478                                 ok            True                  False
  META           63.64               11            2.16             11.52        757.56                53.30         0.599          pass              0.103             12.0                           0.226                2.88              0.283                                 ok           False                  False
  SNPS           77.78                9            2.50              8.66        490.80                50.26         0.589          pass              0.063              1.5                           0.074               10.85              0.632                                 ok           False                  False
   STX           81.82               33            1.22              6.38        744.46                68.64         0.567          pass              0.426             55.9                           0.345              -19.98             -2.458            downtrend_blocked_slope           False                  False
  QCOM           82.61               23            1.77              2.19        175.92                53.60         0.564          pass              0.270             19.1                           0.317               -5.60             -0.606 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           90.91               11            0.86              0.13         20.83                21.61         0.553          pass              0.453             33.3                           0.408               -3.39             -0.365            downtrend_blocked_slope           False                  False
  MSTR           92.31               13            4.30              4.58        150.22                75.74         0.536          pass              0.437             11.7                           0.198               -4.87             -0.739            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-10-14T10:35:03.750968-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T10:30:05.874859-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T10:25:04.858915-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T10:20:06.339818-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T10:15:04.940444-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T10:10:06.594596-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T10:05:04.809604-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T10:00:05.984655-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "ZS261113C00225000", "current_drop_pct": 0.9, "early_entry_score": 0.75, "early_reclaim_pct": 71.2, "entry_ask": 15.55, "entry_bid": 12.5, "entry_mode": "early", "entry_option_price": 14.025, "hypothetical_budget": 67731.15, "hypothetical_contracts": 48, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 15.0, "option_spread_pct": 21.75, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.846, "shadow_only": true, "success_rate": 91.67, "ticker": "ZS", "timing_score": 0.521, "top_candidates": [{"current_drop_pct": 0.9, "early_entry_score": 0.75, "early_reclaim_pct": 71.2, "matched_signals": 36, "recovery_stability_score": 0.846, "success_rate": 91.67, "ticker": "ZS", "timing_score": 0.521, "trend_health_status": "ok"}, {"current_drop_pct": 1.22, "early_entry_score": 0.682, "early_reclaim_pct": 65.5, "matched_signals": 33, "recovery_stability_score": 0.807, "success_rate": 90.91, "ticker": "FTNT", "timing_score": 0.411, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-14T09:50:06.904742-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"asset_type": "option", "contract_symbol": "SNPS261120C00500000", "fill_price": 22.86, "pnl": -7112.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SNPS"}
2026-10-14T00:00:06.708726-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {'saved': 91, 'empty': 2}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261014103503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261014103503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261014103503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261014103503)

</details>
