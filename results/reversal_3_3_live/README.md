# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 11:55:02 EDT`
Last processed slot: `manage_1200`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MNST           95.00               20            1.21              0.75         88.78                49.60         0.633          pass              0.657             42.5                           0.640               -0.58              0.185                                 ok            True                  False
  FTNT          100.00               25            1.63              1.68        146.42                71.69         0.629          pass              0.749             62.0                           0.753               14.42              1.253                                 ok            True                  False
  MELI           91.30               23            1.95             23.68       1720.83                60.28         0.596          pass              0.549             33.6                           0.494                7.01              0.715                                 ok            True                  False
  INTC           97.06               34            0.56              0.43        109.15                88.85         0.587          pass              0.883             88.2                           0.660                0.51             -0.075                                 ok            True                   True
  AMGN           88.24               17            0.94              2.17        328.20                20.27         0.529          pass              0.483             54.6                           0.483                0.51              0.034                                 ok            True                  False
   ADP          100.00               12            2.30              3.76        232.13                34.26         0.506          pass              0.575             37.0                           0.656                2.44              0.303                                 ok            True                  False
  INSM           50.00               12            3.99              2.96        104.76               110.78         0.672          pass              0.149             22.7                           0.436               -4.99             -0.323            downtrend_blocked_slope           False                  False
    ZS          100.00                2            8.95              9.76        151.53               157.27         0.562          pass              0.490             11.3                           0.498              -18.84             -2.815            downtrend_blocked_slope           False                  False
   WMT           82.35               17            1.23              0.99        114.18                32.65         0.562          pass              0.221             18.5                           0.307              -15.11             -1.703 downtrend_blocked_slope_and_streak           False                  False
  REGN           85.71               28            1.02              4.30        598.82                42.53         0.548          pass              0.425             32.7                           0.217               -5.44             -0.652 downtrend_blocked_slope_and_streak           False                  False
   HON           71.43                7            1.70              2.82        235.33                24.20         0.533          pass              0.083              9.7                           0.234                7.03              0.953                                 ok           False                  False
 GOOGL           87.50                8            2.45              6.45        373.61                26.14         0.502          pass              0.396             48.6                           0.383               -7.50             -0.497            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                   detail
2026-06-02T11:55:02.481940-04:00 early_entry_1155 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:50:01.505874-04:00 early_entry_1150 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:45:06.568755-04:00 early_entry_1145 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:40:01.271913-04:00 early_entry_1140 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:35:01.271646-04:00 early_entry_1135 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:30:04.237556-04:00 early_entry_1130 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:25:01.418868-04:00 early_entry_1125 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:25:01.418868-04:00      manage_1130          exit {"asset_type": "option", "contract_symbol": "AMZN260717C00260000", "fill_price": 12.575, "pnl": 2662.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.44, "ticker": "AMZN"}
2026-06-02T11:20:04.407163-04:00 early_entry_1120 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:15:04.236525-04:00 early_entry_1115 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602115502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602115502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602115502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602115502)

</details>
