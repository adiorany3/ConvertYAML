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
1. `AKUN-001-CELESTARA-VLESS-WS-77MS` (url=227ms, nekobox=257ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-80MS` (url=223ms, nekobox=249ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-93MS` (url=217ms, nekobox=259ms, status=yes)
4. `AKUN-004-ZOOM-VLESS-WS-90MS` (url=210ms, nekobox=250ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-90MS` (url=205ms, nekobox=252ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-94MS` (url=235ms, nekobox=261ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-88MS` (url=234ms, nekobox=239ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-102MS` (url=229ms, nekobox=256ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-80MS` (url=209ms, nekobox=238ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-83MS` (url=202ms, nekobox=261ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-113MS` (url=223ms, status=HTTP 204)
12. `AKUN-012-IDC-SG-VLESS-WS-99MS` (url=229ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-95MS` (url=236ms, status=HTTP 204)
14. `AKUN-014-GO-DADDY-COM-LLC-VLESS-WS-114MS` (url=204ms, status=HTTP 204)
15. `AKUN-015-PUBLICDOMAINREGISTRY-NET-VLESS-WS-99MS` (url=224ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-111MS` (url=207ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-113MS` (url=237ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-98MS` (url=245ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-104MS` (url=221ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-127MS` (url=202ms, status=HTTP 204)
21. `AKUN-022-POLICE-VLESS-WS-133MS` (url=219ms, status=HTTP 204)
22. `AKUN-023-POLICE-VLESS-WS-108MS` (url=270ms, status=HTTP 204)
23. `AKUN-024-SPEEDTEST-VLESS-WS-237MS` (url=527ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-257MS` (url=364ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-135MS` (url=225ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
