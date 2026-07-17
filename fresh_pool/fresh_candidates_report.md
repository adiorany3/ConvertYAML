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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-68MS` (url=244ms, nekobox=264ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-70MS` (url=236ms, nekobox=285ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-68MS` (url=239ms, nekobox=273ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS` (url=237ms, nekobox=262ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-71MS` (url=252ms, nekobox=263ms, status=yes)
6. `AKUN-006-DIXONS-VLESS-WS-95MS` (url=253ms, nekobox=276ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-90MS` (url=263ms, nekobox=287ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-95MS` (url=250ms, nekobox=286ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-106MS` (url=276ms, nekobox=283ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-101MS` (url=306ms, nekobox=283ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-120MS` (url=247ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-78MS` (url=245ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-116MS` (url=259ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-103MS` (url=245ms, status=HTTP 204)
15. `AKUN-015-UK-GB-DCL-01-20191003-VLESS-WS-139MS` (url=268ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-118MS` (url=251ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-134MS` (url=230ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-136MS` (url=265ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-116MS` (url=235ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-142MS` (url=297ms, status=HTTP 204)
21. `AKUN-021-WPENG-VLESS-WS-87MS` (url=272ms, status=HTTP 204)
22. `AKUN-022-UK-GB-DCL-01-20191003-VLESS-WS-95MS` (url=289ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-229MS` (url=647ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-284MS` (url=639ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-183MS` (url=298ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
