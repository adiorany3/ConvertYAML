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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-UNKNOWN-VLESS-WS-77MS` (url=201ms, nekobox=255ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-80MS` (url=204ms, nekobox=256ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-85MS` (url=223ms, nekobox=248ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-83MS` (url=209ms, nekobox=233ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-85MS` (url=208ms, nekobox=257ms, status=yes)
6. `AKUN-006-PUBLICDOMAINREGISTRY-NET-VLESS-WS-82MS` (url=226ms, nekobox=243ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-81MS` (url=218ms, nekobox=252ms, status=yes)
8. `AKUN-008-JP-MISAKA-VLESS-WS-89MS` (url=222ms, nekobox=254ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-88MS` (url=243ms, nekobox=313ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-86MS` (url=209ms, nekobox=233ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-91MS` (url=213ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-87MS` (url=228ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-120MS` (url=204ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-124MS` (url=220ms, status=HTTP 204)
15. `AKUN-015-466688-VLESS-WS-88MS` (url=236ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-88MS` (url=229ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-106MS` (url=237ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-101MS` (url=232ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-238MS` (url=571ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-251MS` (url=577ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-250MS` (url=533ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-237MS` (url=638ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-270MS` (url=560ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-263MS` (url=4873ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-303MS` (url=511ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
