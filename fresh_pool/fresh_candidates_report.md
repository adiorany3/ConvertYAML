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
1. `AKUN-001-UNKNOWN-VLESS-WS-65MS` (url=194ms, nekobox=225ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-70MS` (url=200ms, nekobox=235ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=207ms, nekobox=232ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS` (url=220ms, nekobox=267ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-73MS`
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-68MS`
7. `AKUN-007-IDC-SG-VLESS-WS-109MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-80MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS`
10. `AKUN-011-CLOUDFLARE-VLESS-WS-125MS` (url=212ms, nekobox=7177ms, status=no)
11. `AKUN-012-ES-FORNEX-20160629-VLESS-WS-107MS` (url=225ms, nekobox=5157ms, status=no)
12. `AKUN-010-UNKNOWN-VLESS-WS-82MS`
13. `AKUN-014-MEDIUM-VLESS-WS-114MS` (url=219ms, status=HTTP 204)
14. `AKUN-015-VOV-VLESS-WS-145MS` (url=209ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-103MS` (url=215ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-91MS` (url=210ms, status=HTTP 204)
17. `AKUN-018-NEXUSMODS-VLESS-WS-125MS` (url=203ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-106MS` (url=249ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-73MS` (url=218ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-99MS` (url=223ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-97MS` (url=221ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-96MS` (url=216ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-90MS` (url=202ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-238MS` (url=517ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-274MS` (url=357ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
