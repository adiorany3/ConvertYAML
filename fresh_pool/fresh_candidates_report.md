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
1. `AKUN-001-RU-BEGET-VLESS-WS-83MS` (url=210ms, nekobox=243ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-88MS` (url=220ms, nekobox=254ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-91MS` (url=215ms, nekobox=233ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-96MS` (url=254ms, nekobox=237ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-94MS` (url=217ms, nekobox=259ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-93MS` (url=228ms, nekobox=241ms, status=yes)
7. `AKUN-007-WEBEX-VLESS-WS-85MS` (url=200ms, nekobox=254ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-96MS` (url=201ms, nekobox=265ms, status=yes)
9. `AKUN-009-PUBLICDOMAINREGISTRY-NET-VLESS-WS-96MS` (url=244ms, nekobox=281ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-97MS` (url=226ms, nekobox=229ms, status=yes)
11. `AKUN-011-HETZNER-VLESS-WS-105MS` (url=235ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-122MS` (url=224ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-124MS` (url=315ms, status=HTTP 204)
14. `AKUN-014-US-VLESS-WS-103MS` (url=221ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-120MS` (url=255ms, status=HTTP 204)
16. `AKUN-016-466688-VLESS-WS-149MS` (url=207ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-98MS` (url=207ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-132MS` (url=228ms, status=HTTP 204)
19. `AKUN-019-PAGES-VLESS-WS-119MS` (url=230ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-91MS` (url=223ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-243MS` (url=552ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-245MS` (url=609ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-280MS` (url=573ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-288MS` (url=529ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-143MS` (url=223ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
