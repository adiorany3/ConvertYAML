# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 31

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-CLOUDFLARE-VLESS-WS-76MS` (url=269ms, nekobox=338ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS` (url=289ms, nekobox=273ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-82MS` (url=225ms, nekobox=268ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-75MS` (url=252ms, nekobox=264ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-73MS` (url=247ms, nekobox=270ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-78MS` (url=243ms, nekobox=264ms, status=yes)
7. `AKUN-007-COMPREND-NET-VLESS-WS-104MS` (url=251ms, nekobox=284ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-110MS` (url=238ms, nekobox=272ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-80MS` (url=259ms, nekobox=309ms, status=yes)
10. `AKUN-010-466688-VLESS-WS-99MS` (url=248ms, nekobox=264ms, status=yes)
11. `AKUN-011-COMPREND-NET-VLESS-WS-146MS` (url=259ms, status=HTTP 204)
12. `AKUN-012-COMPREND-NET-VLESS-WS-102MS` (url=263ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-121MS` (url=266ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-276MS` (url=613ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-260MS` (url=578ms, status=HTTP 204)
16. `AKUN-017-WPENG-VLESS-WS-290MS` (url=627ms, status=HTTP 204)
17. `AKUN-018-SPEEDTEST-VLESS-WS-290MS` (url=602ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-301MS` (url=678ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-303MS` (url=675ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-396MS` (url=512ms, status=HTTP 204)
21. `AKUN-022-BIGCOMMERCE-VLESS-WS-474MS` (url=776ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-462MS` (url=567ms, status=HTTP 204)
23. `AKUN-028-UNKNOWN-VLESS-WS-521MS` (url=886ms, status=HTTP 204)
24. `AKUN-033-UNKNOWN-VLESS-WS-593MS` (url=5247ms, status=HTTP 204)
25. `AKUN-034-UNKNOWN-VLESS-WS-631MS` (url=917ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
