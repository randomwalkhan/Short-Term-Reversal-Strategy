# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-08 11:05:04 EDT`
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

- Cash: `$108,579.30`
- Equity: `$108,579.30`
- Realized PnL: `$98,579.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-08)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  NVDA     option         option NVDA261120C00235000     40          2026-10-07         2026-10-08       13.075     11.7675 -5230.0  -10.000000        stop_loss_hit_at_scan
  ABNB     option         option ABNB261120C00160000     55          2026-10-06         2026-10-08        9.475     11.0500  8662.5   16.622691 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           86.36               22            1.37              2.87        298.36                58.54         0.580            pass              0.387             26.6                           0.147               12.94              1.446                                 ok            True                  False
  CSCO           88.46               26            0.76              0.63        117.12                34.80         0.554            pass              0.493             35.1                           0.337                9.33              1.195                                 ok            True                  False
  MPWR           87.50               24            2.04             20.33       1417.27                55.22         0.552            pass              0.457             36.0                           0.369                4.75              0.832                                 ok            True                  False
   ADI           90.91               33            0.69              1.99        409.23                34.70         0.502            pass              0.693             66.1                           0.582                6.44              0.739                                 ok            True                   True
   TRI           87.88               33            0.97              0.67         98.99                44.07         0.500 below_threshold              0.593             59.8                           0.613               -1.99             -0.041                                 ok            True                  False
  UPRO           82.76               29            0.78              0.85        154.79                30.53         0.500            pass              0.420             56.7                           0.341                2.64              0.421                                 ok            True                  False
  MSTR           91.89               37            0.73              0.78        153.04                80.80         0.629            pass              0.800             80.1                           0.773               -5.79             -0.116           downtrend_blocked_streak           False                  False
  QCOM           87.50               24            1.83              2.28        176.14                56.66         0.576            pass              0.439             29.2                           0.363              -10.50             -1.106 downtrend_blocked_slope_and_streak           False                  False
  META           85.71               42            0.03              0.13        721.25                52.76         0.550            pass              0.702             98.4                           0.506               -7.26             -0.394            downtrend_blocked_slope           False                  False
  SOXL           79.17               24            5.39              5.99        156.34               112.38         0.534            pass              0.241             31.6                           0.218                2.75              0.984                                 ok           False                  False
   STX           88.89               27            2.47             13.96        801.59                69.74         0.533            pass              0.459             18.4                           0.154              -13.06             -1.593            downtrend_blocked_slope           False                  False
   WDC           81.82               44            0.40              1.13        404.94                65.89         0.531            pass              0.545             81.3                           0.534              -10.33             -1.326            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-10-08T11:05:04.028696-04:00 early_entry_1105 early_entry_shadow                      {"contract_symbol": "ADI261120C00400000", "current_drop_pct": 0.69, "early_entry_score": 0.693, "early_reclaim_pct": 66.1, "entry_ask": 27.9, "entry_bid": 25.0, "entry_mode": "early", "entry_option_price": 26.45, "hypothetical_budget": 54289.65, "hypothetical_contracts": 20, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 121.0, "option_spread_pct": 10.96, "option_volume": 23.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.582, "shadow_only": true, "success_rate": 90.91, "ticker": "ADI", "timing_score": 0.502, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.693, "early_reclaim_pct": 66.1, "matched_signals": 33, "recovery_stability_score": 0.582, "success_rate": 90.91, "ticker": "ADI", "timing_score": 0.502, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-08T11:00:06.101046-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:55:06.968008-04:00 early_entry_1055 early_entry_shadow {"contract_symbol": "ISRG261120C00410000", "current_drop_pct": 0.58, "early_entry_score": 0.736, "early_reclaim_pct": 64.7, "entry_ask": 26.4, "entry_bid": 23.5, "entry_mode": "early", "entry_option_price": 24.95, "hypothetical_budget": 54289.65, "hypothetical_contracts": 21, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 121.0, "option_spread_pct": 11.62, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.623, "shadow_only": true, "success_rate": 91.89, "ticker": "ISRG", "timing_score": 0.447, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.736, "early_reclaim_pct": 64.7, "matched_signals": 37, "recovery_stability_score": 0.623, "success_rate": 91.89, "ticker": "ISRG", "timing_score": 0.447, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-08T10:50:05.913383-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:45:06.914386-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:40:05.011138-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:35:07.119041-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:35:07.119041-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"asset_type": "option", "contract_symbol": "ABNB261120C00160000", "fill_price": 11.05, "pnl": 8662.5, "reason": "take_profit_day2_hit_at_scan", "return_pct": 16.62, "ticker": "ABNB"}
2026-10-08T10:30:06.096812-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:25:06.880454-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261008110504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261008110504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261008110504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261008110504)

</details>
