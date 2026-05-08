# Reversal 3.3.2 Live Paper Test

Latest checkpoint (ET): `2026-05-08 10:50:06 EDT`
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

- Cash: `$29,983.50`
- Equity: `$29,983.50`
- Realized PnL: `$19,983.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-08)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   TXN     option         option TXN260618C00290000     10          2026-05-07         2026-05-08         13.1        15.5 2400.0   18.320611 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate
  FAST           96.00               25            0.77              0.24         44.26                33.68         0.551            pass               -0.97             -0.073                                 ok            True
   ADP           84.21               19            1.24              1.86        213.29                38.09         0.520            pass                7.58              0.698                                 ok            True
    ZS           80.77               26            1.92              2.06        151.91                60.77         0.516            pass               10.59              1.151                                 ok            True
  CHTR           89.19               37            0.84              0.95        159.83               119.32         0.776            pass              -11.79             -1.161            downtrend_blocked_slope           False
 CMCSA           87.50                8            1.68              0.31         26.11                61.43         0.708            pass               -6.39             -0.612 downtrend_blocked_slope_and_streak           False
  SHOP           88.00               25            2.18              1.70        111.01                82.33         0.607            pass              -13.13             -1.594 downtrend_blocked_slope_and_streak           False
  MSFT           80.00               20            1.35              3.98        419.22                34.38         0.536            pass               -2.21             -0.279            downtrend_blocked_slope           False
  PYPL           94.12               34            0.61              0.20         46.14                42.03         0.529            pass               -8.99             -1.051 downtrend_blocked_slope_and_streak           False
  META           75.76               33            0.81              3.49        615.31                41.17         0.521            pass               -9.36             -1.228 downtrend_blocked_slope_and_streak           False
  NFLX           90.24               41            0.62              0.38         88.10                43.15         0.512            pass               -5.11             -0.597            downtrend_blocked_slope           False
  TMUS           88.10               42            0.19              0.25        194.09                36.72         0.501            pass                2.13              0.368                                 ok           False
   XEL           90.00               30            0.49              0.28         80.31                27.43         0.497 below_threshold                1.12              0.173                                 ok           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                               detail
2026-05-08T10:40:01.112958-04:00 manage_1030 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T10:35:06.124944-04:00 manage_1030 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T10:30:05.923430-04:00 manage_1030 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T10:25:01.121300-04:00 manage_1030 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T10:20:05.936337-04:00 manage_1030         exit {"asset_type": "option", "contract_symbol": "TXN260618C00290000", "fill_price": 15.5, "pnl": 2400.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.32, "ticker": "TXN"}
2026-05-08T10:10:01.121937-04:00 manage_1000 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T10:05:06.101764-04:00 manage_1000 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T10:00:06.094621-04:00 manage_1000 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T09:55:06.107419-04:00 manage_1000 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T09:40:05.918205-04:00 manage_0930 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260508105006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260508105006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260508105006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260508105006)

</details>
