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
1. `AKUN-001-ORACLE-VLESS-WS-65MS` (url=226ms, nekobox=258ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=237ms, nekobox=275ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-70MS` (url=253ms, nekobox=299ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-64MS` (url=237ms, nekobox=270ms, status=yes)
5. `AKUN-005-WPENG-VLESS-WS-77MS` (url=268ms, nekobox=286ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-81MS` (url=247ms, nekobox=270ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-104MS` (url=242ms, nekobox=267ms, status=yes)
8. `AKUN-008-CZ-LOTUNA-19970206-VLESS-WS-97MS` (url=256ms, nekobox=276ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-84MS` (url=243ms, nekobox=268ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-99MS` (url=239ms, nekobox=279ms, status=yes)
11. `AKUN-011-466688-VLESS-WS-117MS` (url=303ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-105MS` (url=284ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-117MS` (url=275ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-99MS` (url=250ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-82MS` (url=250ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-124MS` (url=249ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-108MS` (url=241ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-127MS` (url=249ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-107MS` (url=252ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-119MS` (url=237ms, status=HTTP 204)
21. `AKUN-021-CZ-LOTUNA-19970206-VLESS-WS-86MS` (url=275ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-88MS` (url=305ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-125MS` (url=290ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-124MS` (url=241ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-83MS` (url=240ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
