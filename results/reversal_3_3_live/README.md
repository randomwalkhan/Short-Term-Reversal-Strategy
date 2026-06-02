# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 11:25:01 EDT`
Last processed slot: `manage_1130`

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
  MNST           93.75               16            1.49              0.93         88.70                49.60         0.640          pass              0.557             28.8                           0.442               -0.87              0.172                                 ok            True                  False
  MELI           89.47               19            2.09             25.30       1720.14                60.28         0.612          pass              0.461             29.1                           0.275                6.87              0.708                                 ok            True                  False
  INTC           97.06               34            0.78              0.60        109.07                88.85         0.572          pass              0.868             83.5                           0.730                0.29             -0.085                                 ok            True                   True
  CDNS          100.00               11            2.43              7.04        411.14                44.19         0.548          pass              0.532             23.4                           0.241               16.80              1.702                                 ok            True                  False
  AMGN           90.00               20            0.80              1.84        328.34                20.27         0.520          pass              0.570             61.5                           0.610                0.65              0.040                                 ok            True                  False
   ADP          100.00               10            2.52              4.13        231.97                34.26         0.505          pass              0.543             30.8                           0.636                2.20              0.293                                 ok            True                  False
  FTNT          100.00                9            2.31              2.38        146.12                71.69         0.689          pass              0.608             46.2                           0.443               13.63              1.222                                 ok           False                  False
  INSM           45.45               11            4.12              3.06        104.72               110.78         0.665          pass              0.134             20.2                           0.226               -5.12             -0.329            downtrend_blocked_slope           False                  False
   WMT           76.92               13            1.33              1.07        114.14                32.65         0.576          pass              0.113             11.9                           0.250              -15.20             -1.708 downtrend_blocked_slope_and_streak           False                  False
  REGN           89.19               37            0.38              1.59        599.98                42.53         0.535          pass              0.704             75.2                           0.677               -4.83             -0.622 downtrend_blocked_slope_and_streak           False                  False
   HON           71.43                7            1.75              2.91        235.29                24.20         0.530          pass              0.074              7.1                           0.235                6.98              0.951                                 ok           False                  False
    ZS          100.00                1            9.76             10.63        151.15               157.27         0.513          pass              0.461              3.3                           0.160              -19.56             -2.856            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-06-02T11:25:01.418868-04:00 early_entry_1125 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T11:25:01.418868-04:00      manage_1130          exit                                                                                                                                                                                                                                             {"asset_type": "option", "contract_symbol": "AMZN260717C00260000", "fill_price": 12.575, "pnl": 2662.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.44, "ticker": "AMZN"}
2026-06-02T11:20:04.407163-04:00 early_entry_1120 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T11:15:04.236525-04:00 early_entry_1115 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T11:10:04.323542-04:00 early_entry_1110 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T11:05:01.381854-04:00 early_entry_1105 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T11:00:04.363054-04:00 early_entry_1100 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T10:55:06.617729-04:00 early_entry_1055 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T10:50:06.041869-04:00 early_entry_1050 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T10:45:01.434257-04:00 early_entry_1045         entry {"allocated_cash": 16200.0, "asset_type": "option", "contract_symbol": "AMZN260717C00260000", "contracts": 15, "early_entry_score": 0.702, "entry_mode": "early", "entry_option_price": 10.8, "execution_mode": "option", "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 8913.0, "option_spread_pct": 1.85, "option_volume": 913.0, "success_rate": 90.62, "ticker": "AMZN", "timing_score": 0.457}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602112501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602112501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602112501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602112501)

</details>
