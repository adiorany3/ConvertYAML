# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-UNKNOWN-VLESS-WS-87MS` (url=226ms, nekobox=229ms, status=yes)
2. `AKUN-002-HETZNER-VLESS-WS-73MS` (url=231ms, nekobox=251ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-95MS` (url=231ms, nekobox=255ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-108MS` (url=206ms, nekobox=259ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-105MS` (url=221ms, nekobox=228ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-104MS` (url=211ms, nekobox=251ms, status=yes)
7. `AKUN-007-877774-VLESS-WS-99MS` (url=214ms, nekobox=255ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-85MS` (url=230ms, nekobox=236ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-129MS` (url=223ms, nekobox=243ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-143MS` (url=204ms, nekobox=230ms, status=yes)
11. `AKUN-011-FASTVPSUS-IPV4-VLESS-WS-191MS` (url=248ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-256MS` (url=548ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-280MS` (url=374ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-114MS` (url=215ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-339MS` (url=728ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-599MS` (url=987ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-617MS` (url=1044ms, status=HTTP 204)
18. `AKUN-021-UNKNOWN-VLESS-WS-681MS` (url=1076ms, status=HTTP 204)
19. `AKUN-023-CLOUDFLARE-VLESS-WS-701MS` (url=1183ms, status=HTTP 204)
20. `AKUN-024-UNKNOWN-VLESS-WS-703MS` (url=1141ms, status=HTTP 204)
21. `AKUN-026-CLOUDFLARE-VLESS-WS-725MS` (url=1517ms, status=HTTP 204)
22. `AKUN-027-CLOUDFLARE-VLESS-WS-641MS` (url=1074ms, status=HTTP 204)
23. `AKUN-028-CLOUDFLARE-VLESS-WS-740MS` (url=1172ms, status=HTTP 204)
24. `AKUN-029-CLOUDFLARE-VLESS-WS-720MS` (url=1095ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
