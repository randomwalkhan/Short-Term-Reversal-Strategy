# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-18 12:50:01 EDT`
Last processed slot: `manage_1300`

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

- Cash: `$15,642.50`
- Equity: `$29,142.50`
- Realized PnL: `$19,192.50`
- Unrealized PnL: `$-50.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TTWO     option         option TTWO260618C00250000       2026-05-18                   0     10     13550.0                 13500.0        13.55           13.5      241.03        241.86          bid_ask_mid                       13.5                bid_ask_mid                    True           -50.0                  -0.37         97.62               42              0.58         61.06           59.51                  33.53                3069.0           22.0               0.11                      ok
```

## Today's Closed Trades (2026-05-18)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CDNS     option         option CDNS260618C00330000      5          2026-05-15         2026-05-18        29.05      26.145 -1452.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           82.35               34            0.51              1.04        291.05                90.58         0.725            pass              0.404             36.3                           0.308               -0.26             -0.059                                 ok            True                  False
   TXN           92.00               25            0.81              1.72        301.99                68.84         0.698            pass              0.602             37.4                           0.281                7.44              0.921                                 ok            True                  False
  QCOM           89.47               19            1.86              2.63        200.36                99.06         0.667            pass              0.537             52.5                           0.432               17.43              1.171                                 ok            True                  False
  INTC          100.00               20            2.69              2.05        107.89               115.99         0.663            pass              0.655             40.5                           0.568               10.51              0.682                                 ok            True                  False
  CSCO           91.30               23            1.18              0.97        117.79                49.84         0.601            pass              0.557             36.2                           0.308               26.11              2.716                                 ok            True                  False
  SNPS           95.83               24            1.76              6.18        499.77                42.05         0.522            pass              0.647             33.8                           0.456               -0.79              0.003                                 ok            True                  False
  AAPL           85.71               14            1.63              3.42        298.76                22.88         0.519            pass              0.255              8.1                           0.184                6.78              0.682                                 ok            True                  False
  INSM           66.67               24            2.51              1.91        108.32               111.34         0.630            pass              0.279             41.1                           0.574              -24.00             -2.268 downtrend_blocked_slope_and_streak           False                  False
  MCHP           80.77               26            1.34              0.88         93.47                53.01         0.534            pass              0.205              8.0                           0.123               -2.84             -0.569 downtrend_blocked_slope_and_streak           False                  False
  META           74.19               31            0.86              3.70        612.65                37.75         0.499 below_threshold              0.387             65.6                           0.582               -0.24              0.059                                 ok           False                  False
  AMGN           82.61               23            0.71              1.63        325.61                26.25         0.490 below_threshold              0.368             54.3                           0.643                0.80              0.122                                 ok           False                  False
  ASML           85.00               20            2.49             26.18       1490.59                50.55         0.487 below_threshold              0.292             14.4                           0.270                5.64              0.499                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                             detail
2026-05-18T12:00:03.667934-04:00 early_entry_1200 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:55:01.697815-04:00 early_entry_1155 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:50:04.542688-04:00 early_entry_1150 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:45:01.537610-04:00 early_entry_1145 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:40:04.531844-04:00 early_entry_1140 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:35:01.580218-04:00 early_entry_1135 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:30:01.530896-04:00 early_entry_1130 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:25:06.197767-04:00 early_entry_1125 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:25:06.197767-04:00      manage_1130          exit {"asset_type": "option", "contract_symbol": "CDNS260618C00330000", "fill_price": 26.145, "pnl": -1452.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CDNS"}
2026-05-18T11:20:01.549476-04:00 early_entry_1120 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260518125001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260518125001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260518125001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260518125001)

</details>
