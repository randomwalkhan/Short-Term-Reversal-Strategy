# Reversal 3.4.1 Live Paper Test

Latest checkpoint (ET): `2026-05-11 10:12:01 EDT`
Last processed slot: `early_entry_1010`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$16,593.50`
- Equity: `$30,978.50`
- Realized PnL: `$22,833.50`
- Unrealized PnL: `$-1,855.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG260618C00290000       2026-05-11                   0      7     16240.0                 14385.0         23.2          20.55      301.86        300.27         -1855.0                 -11.42         89.74               39              0.58         46.89           42.66                  48.41                 991.0           18.0               0.15                      ok
```

## Today's Closed Trades (2026-05-11)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  NXPI           80.56               36            0.73              1.51        294.10                87.07         0.698          pass              0.385             42.4                           0.228               23.52              1.917                      ok            True                  False
  TEAM           81.82               22            3.99              2.56         90.50               114.36         0.626          pass              0.215              7.9                           0.083               27.05              3.323                      ok            True                  False
  GOOG           85.71               21            1.40              3.90        395.38                37.66         0.567          pass              0.382             33.2                           0.329               12.32              1.430                      ok            True                  False
   ADP           90.91               22            1.03              1.54        212.33                34.95         0.538          pass              0.568             47.9                           0.285                6.88              0.478                      ok            True                  False
  MRVL          100.00               24            1.61              1.91        169.31                55.66         0.536          pass              0.741             64.7                           0.628                5.81              0.792                      ok            True                  False
  TMUS           86.21               29            0.87              1.18        193.13                36.59         0.536          pass              0.461             38.2                           0.374                5.03              0.270                      ok            True                  False
    ZS           82.86               35            1.28              1.37        151.54                58.64         0.532          pass              0.321              8.5                           0.139               11.98              1.383                      ok            True                  False
   WMT           87.50               16            1.20              1.10        129.96                19.38         0.529          pass              0.324             10.3                           0.237                1.19              0.156                      ok            True                  False
  ASML           84.62               13            3.33             37.12       1576.11                48.89         0.503          pass              0.217              8.0                           0.180                7.44              1.203                      ok            True                  False
  MDLZ           84.62               26            0.60              0.26         61.44                24.76         0.500          pass              0.510             76.7                           0.512                6.55              0.495                      ok            True                  False
  CHTR           85.00               20            2.13              2.31        153.87               119.48         0.789          pass              0.407             42.6                           0.687              -13.20             -1.194 downtrend_blocked_slope           False                  False
  SHOP           92.31               13            4.29              3.32        109.08                82.28         0.580          pass              0.419              4.2                           0.107              -14.87             -1.727 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-05-11T10:12:01.604493-04:00 early_entry_1010 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T10:05:43.962541-04:00 early_entry_1005         entry {"allocated_cash": 16240.0, "asset_type": "option", "contract_symbol": "CEG260618C00290000", "contracts": 7, "early_entry_score": 0.766, "entry_mode": "early", "entry_option_price": 23.2, "execution_mode": "option", "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 991.0, "option_spread_pct": 14.66, "option_volume": 18.0, "success_rate": 89.74, "ticker": "CEG", "timing_score": 0.357}
2026-05-11T09:18:42.943466-04:00     data_refresh  data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                    {'saved': 92}
2026-05-08T16:05:06.142170-04:00      manage_1600          exit                                                                                                                                                                                                                                           {"asset_type": "option", "contract_symbol": "TEAM260618C00090000", "fill_price": 9.25, "pnl": 2850.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 19.35, "ticker": "TEAM"}
2026-05-08T16:00:06.094263-04:00      manage_1600  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-05-08T15:55:02.084715-04:00      manage_1600  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-05-08T15:40:02.063692-04:00      manage_1530  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-05-08T15:35:05.923584-04:00      manage_1530  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-05-08T15:30:06.082521-04:00      manage_1530  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-05-08T15:25:06.105856-04:00      manage_1530  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260511101201)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260511101201)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260511101201)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260511101201)

</details>
