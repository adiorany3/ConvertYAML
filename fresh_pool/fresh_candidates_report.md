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
1. `AKUN-001-UNKNOWN-VLESS-WS-91MS` (url=223ms, nekobox=248ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-92MS` (url=210ms, nekobox=244ms, status=yes)
3. `AKUN-003-PUBLICDOMAINREGISTRY-NET-VLESS-WS-93MS` (url=214ms, nekobox=264ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-97MS` (url=222ms, nekobox=243ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-98MS` (url=209ms, nekobox=251ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-99MS` (url=264ms, nekobox=269ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-98MS` (url=240ms, nekobox=253ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-104MS` (url=253ms, nekobox=267ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-110MS` (url=261ms, nekobox=267ms, status=yes)
10. `AKUN-010-466688-VLESS-WS-127MS` (url=245ms, nekobox=295ms, status=yes)
11. `AKUN-011-MEDIUM-VLESS-WS-125MS` (url=224ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-129MS` (url=240ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-125MS` (url=229ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-146MS` (url=218ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-121MS` (url=251ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-125MS` (url=225ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-111MS` (url=223ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-118MS` (url=267ms, status=HTTP 204)
19. `AKUN-019-1PASSWORD-VLESS-WS-123MS` (url=248ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-144MS` (url=289ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-130MS` (url=215ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-104MS` (url=243ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-119MS` (url=249ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-108MS` (url=220ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-118MS` (url=236ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
