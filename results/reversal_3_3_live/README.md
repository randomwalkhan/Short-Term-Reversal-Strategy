# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 14:25:01 EDT`
Last processed slot: `manage_1430`

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

- Cash: `$36,331.75`
- Equity: `$36,331.75`
- Realized PnL: `$26,331.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-02)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AMZN     option         option AMZN260717C00260000     15          2026-06-02         2026-06-02         10.8      12.575 2662.5   16.435185 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MNST           96.00               25            0.84              0.53         88.87                49.60         0.625            pass              0.742             59.9                           0.571               -0.21              0.202                                 ok            True                  False
  FTNT          100.00               42            0.65              0.67        146.85                71.69         0.578            pass              0.912             84.9                           0.644               15.56              1.298                                 ok            True                   True
  INTC           96.15               26            1.65              1.26        108.79                88.85         0.566            pass              0.759             65.1                           0.722               -0.59             -0.125                                 ok            True                  False
   HON           85.00               20            0.84              1.39        235.95                24.20         0.516            pass              0.419             55.7                           0.659                7.98              0.993                                 ok            True                  False
  INSM           66.67               18            2.71              2.01        105.17               110.78         0.729            pass              0.269             47.4                           0.801               -3.73             -0.263            downtrend_blocked_slope           False                  False
  MELI           85.71                7            3.62             43.87       1712.18                60.28         0.576            pass              0.234              8.2                           0.336                5.20              0.637                                 ok           False                  False
   WMT           84.21               19            1.02              0.82        114.25                32.65         0.565            pass              0.326             32.4                           0.432              -14.93             -1.694 downtrend_blocked_slope_and_streak           False                  False
    ZS           66.67                3            8.42              9.18        151.78               157.27         0.552            pass              0.105             16.5                           0.269              -18.37             -2.789            downtrend_blocked_slope           False                  False
  REGN           86.21               29            0.93              3.90        598.99                42.53         0.548            pass              0.464             39.1                           0.383               -5.35             -0.647 downtrend_blocked_slope_and_streak           False                  False
  PAYX           88.89                9            1.98              1.42        101.83                33.30         0.511            pass              0.434             48.5                           0.569                6.27              0.629                                 ok           False                  False
  ISRG           83.33               12            2.39              6.91        409.30                38.26         0.504            pass              0.263             36.7                           0.506               -8.53             -0.917 downtrend_blocked_slope_and_streak           False                  False
  DXCM           73.68               19            1.94              1.01         74.44                46.68         0.498 below_threshold              0.221             37.0                           0.451               12.80              1.028                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                   detail
2026-06-02T12:00:02.493429-04:00 early_entry_1200 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:55:02.481940-04:00 early_entry_1155 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:50:01.505874-04:00 early_entry_1150 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:45:06.568755-04:00 early_entry_1145 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:40:01.271913-04:00 early_entry_1140 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:35:01.271646-04:00 early_entry_1135 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:30:04.237556-04:00 early_entry_1130 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:25:01.418868-04:00 early_entry_1125 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:25:01.418868-04:00      manage_1130          exit {"asset_type": "option", "contract_symbol": "AMZN260717C00260000", "fill_price": 12.575, "pnl": 2662.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.44, "ticker": "AMZN"}
2026-06-02T11:20:04.407163-04:00 early_entry_1120 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602142501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602142501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602142501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602142501)

</details>
