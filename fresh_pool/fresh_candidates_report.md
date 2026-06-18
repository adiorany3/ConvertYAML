# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 19
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 25

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
1. `AKUN-001-UNKNOWN-VLESS-WS-79MS` (url=219ms, nekobox=246ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-93MS` (url=229ms, nekobox=275ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-89MS` (url=202ms, nekobox=229ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-88MS` (url=223ms, nekobox=245ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-111MS` (url=227ms, nekobox=236ms, status=yes)
6. `AKUN-006-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-77MS` (url=219ms, nekobox=251ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-111MS` (url=225ms, nekobox=228ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-104MS` (url=200ms, nekobox=246ms, status=yes)
9. `AKUN-009-DE-138-124-32-VLESS-WS-124MS` (url=223ms, nekobox=263ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-270MS` (url=612ms, nekobox=611ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-303MS` (url=611ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-306MS` (url=599ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-299MS` (url=6289ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-324MS` (url=674ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-316MS` (url=2289ms, status=HTTP 204)
16. `AKUN-017-JISON-VLESS-WS-372MS` (url=766ms, status=HTTP 204)
17. `AKUN-026-PLUSMUSICAL8-VLESS-WS-520MS` (url=2773ms, status=HTTP 204)
18. `AKUN-029-CLOUDFLARE-VLESS-WS-604MS` (url=1027ms, status=HTTP 204)
19. `AKUN-035-CLOUDFLARE-VLESS-WS-471MS` (url=699ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
