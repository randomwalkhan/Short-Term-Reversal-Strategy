# Reversal 3.3.2 Live Paper Test

Latest checkpoint (ET): `2026-05-08 10:55:06 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate
  FAST           96.15               26            0.69              0.21         44.27                33.68         0.550          pass               -0.90             -0.070                                 ok            True
   ADP           84.21               19            1.27              1.91        213.27                38.09         0.518          pass                7.55              0.696                                 ok            True
    ZS           82.14               28            1.73              1.85        152.00                60.77         0.517          pass               10.81              1.160                                 ok            True
   XEL           92.86               28            0.57              0.32         80.29                27.43         0.509          pass                1.04              0.170                                 ok            True
  CHTR           89.19               37            0.82              0.92        159.85               119.32         0.778          pass              -11.77             -1.160            downtrend_blocked_slope           False
 CMCSA           88.89                9            1.51              0.28         26.12                61.43         0.713          pass               -6.22             -0.604 downtrend_blocked_slope_and_streak           False
  SHOP           90.62               32            1.66              1.30        111.18                82.33         0.599          pass              -12.68             -1.570 downtrend_blocked_slope_and_streak           False
  MSFT           78.26               23            1.10              3.24        419.53                34.38         0.530          pass               -1.96             -0.268            downtrend_blocked_slope           False
  PYPL           94.87               39            0.35              0.11         46.17                42.03         0.515          pass               -8.76             -1.039 downtrend_blocked_slope_and_streak           False
  META           77.14               35            0.75              3.23        615.43                41.17         0.514          pass               -9.31             -1.225 downtrend_blocked_slope_and_streak           False
  NFLX           90.70               43            0.55              0.34         88.12                43.15         0.505          pass               -5.04             -0.593            downtrend_blocked_slope           False
  TMUS           87.80               41            0.22              0.30        194.07                36.72         0.505          pass                2.09              0.367                                 ok           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                               detail
2026-05-08T10:55:06.709413-04:00 manage_1100 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T10:40:01.112958-04:00 manage_1030 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T10:35:06.124944-04:00 manage_1030 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T10:30:05.923430-04:00 manage_1030 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T10:25:01.121300-04:00 manage_1030 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T10:20:05.936337-04:00 manage_1030         exit {"asset_type": "option", "contract_symbol": "TXN260618C00290000", "fill_price": 15.5, "pnl": 2400.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.32, "ticker": "TXN"}
2026-05-08T10:10:01.121937-04:00 manage_1000 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T10:05:06.101764-04:00 manage_1000 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T10:00:06.094621-04:00 manage_1000 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
2026-05-08T09:55:06.107419-04:00 manage_1000 slot_skipped                                                                                                                                                      {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260508105506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260508105506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260508105506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260508105506)

</details>
