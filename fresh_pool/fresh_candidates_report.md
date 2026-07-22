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
1. `AKUN-001-UNKNOWN-VLESS-WS-64MS` (url=217ms, nekobox=281ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-83MS` (url=207ms, nekobox=237ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-75MS` (url=223ms, nekobox=190ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-71MS`
5. `AKUN-004-ZOOM-VLESS-WS-83MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-74MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-62MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-64MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-74MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-77MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-93MS`
12. `AKUN-012-DEV-VLESS-WS-108MS` (url=225ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-100MS` (url=221ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-124MS` (url=230ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-78MS` (url=218ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-137MS` (url=228ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-73MS` (url=214ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-75MS` (url=197ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-146MS` (url=239ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-139MS` (url=222ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-150MS` (url=199ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-133MS` (url=201ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-228MS` (url=541ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-253MS` (url=651ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-449MS` (url=1032ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
