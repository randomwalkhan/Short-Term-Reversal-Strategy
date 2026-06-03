# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 10:55:06 EDT`
Last processed slot: `manage_1100`

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
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$34,571.75`
- Equity: `$34,571.75`
- Realized PnL: `$24,571.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-03)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   TXN     option         option TXN260717C00310000      8          2026-06-03         2026-06-03         22.0        19.8 -1760.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CSCO           96.43               28            0.54              0.48        127.79                53.71         0.619          pass              0.824             80.7                           0.761               10.34              0.931                                 ok            True                  False
  MELI           93.94               33            1.07             12.58       1667.44                61.01         0.593          pass              0.715             43.5                           0.510                3.76              0.360                                 ok            True                  False
  FTNT          100.00               40            0.73              0.76        148.54                71.83         0.562          pass              0.901             81.6                           0.662               15.78              1.532                                 ok            True                   True
  WDAY           81.82               22            2.72              2.83        147.67                75.59         0.526          pass              0.273             30.7                           0.391               11.98              2.081                                 ok            True                  False
  MCHP           96.00               25            0.97              0.66         96.68                44.80         0.525          pass              0.756             68.0                           0.631                5.11              0.387                                 ok            True                  False
  CRWD           82.35               17            1.88             10.11        764.62                51.19         0.524          pass              0.300             46.2                           0.585               22.31              2.214                                 ok            True                  False
  AAPL           94.44               18            1.05              2.31        314.21                17.72         0.522          pass              0.496              1.9                           0.157                4.33              0.388                                 ok            True                  False
  UPRO           92.31               26            1.28              1.35        150.29                28.22         0.505          pass              0.582             32.2                           0.350                9.00              0.895                                 ok            True                  False
  INSM           78.57               42            0.52              0.38        103.57               108.46         0.745          pass              0.497             74.3                           0.345               -3.93             -0.407 downtrend_blocked_slope_and_streak           False                  False
    ZS           60.00                5            5.81              5.86        141.64               159.87         0.732          pass              0.103              9.9                           0.296              -22.52             -2.912            downtrend_blocked_slope           False                  False
  INTU           73.68               19            2.93              6.61        319.31               101.75         0.657          pass              0.186             19.9                           0.371              -21.77             -1.278            downtrend_blocked_slope           False                  False
  NXPI           97.30               37            0.32              0.73        323.31                50.93         0.555          pass              0.874             79.4                           0.592                9.61              0.700                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-06-03T10:55:06.117581-04:00 early_entry_1055 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-06-03T10:50:06.086321-04:00 early_entry_1050 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-06-03T10:45:02.015884-04:00 early_entry_1045 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-06-03T10:40:06.216111-04:00 early_entry_1040 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-06-03T10:35:05.540454-04:00 early_entry_1035 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-06-03T10:30:02.209101-04:00 early_entry_1030 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-06-03T10:25:05.972496-04:00 early_entry_1025 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-06-03T10:20:06.156013-04:00 early_entry_1020 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-06-03T10:20:06.156013-04:00      manage_1030          exit                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "TXN260717C00310000", "fill_price": 19.8, "pnl": -1760.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TXN"}
2026-06-03T10:15:06.039702-04:00 early_entry_1015         entry {"allocated_cash": 17600.0, "asset_type": "option", "contract_symbol": "TXN260717C00310000", "contracts": 8, "early_entry_score": 0.813, "entry_mode": "early", "entry_option_price": 22.0, "execution_mode": "option", "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 1851.0, "option_spread_pct": 10.0, "option_volume": 30.0, "success_rate": 100.0, "ticker": "TXN", "timing_score": 0.547}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603105506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603105506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603105506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603105506)

</details>
