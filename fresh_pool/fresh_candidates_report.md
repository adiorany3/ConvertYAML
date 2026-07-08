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
1. `AKUN-001-ORACLE-VLESS-WS-94MS` (url=259ms, nekobox=251ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-98MS` (url=203ms, nekobox=258ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-94MS` (url=233ms, nekobox=265ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-111MS` (url=246ms, nekobox=248ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-100MS` (url=218ms, nekobox=272ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-109MS` (url=267ms, nekobox=274ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-116MS` (url=234ms, nekobox=275ms, status=yes)
8. `AKUN-008-ZOOM-VLESS-WS-118MS` (url=239ms, nekobox=251ms, status=yes)
9. `AKUN-009-WEBEX-VLESS-WS-106MS` (url=234ms, nekobox=282ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-111MS` (url=296ms, nekobox=275ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-130MS` (url=255ms, status=HTTP 204)
12. `AKUN-012-PUBLICDOMAINREGISTRY-NET-VLESS-WS-117MS` (url=241ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-124MS` (url=291ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-106MS` (url=260ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-120MS` (url=235ms, status=HTTP 204)
16. `AKUN-016-OVH-VLESS-WS-115MS` (url=286ms, status=HTTP 204)
17. `AKUN-017-WEBEX-VLESS-WS-100MS` (url=317ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-142MS` (url=282ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-366MS` (url=773ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-397MS` (url=795ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-288MS` (url=560ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-412MS` (url=899ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-426MS` (url=937ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-380MS` (url=806ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-709MS` (url=1145ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
