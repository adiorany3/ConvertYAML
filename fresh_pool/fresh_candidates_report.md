# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 20
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 24

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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-104MS` (url=2450ms, nekobox=1703ms, status=yes)
2. `AKUN-002-SOSKEYNETS-VLESS-WS-102MS` (url=1333ms, nekobox=337ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-105MS` (url=1682ms, nekobox=828ms, status=yes)
4. `AKUN-004-ZOOM-VLESS-WS-105MS` (url=1011ms, nekobox=835ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-121MS` (url=255ms, nekobox=832ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-121MS` (url=942ms, nekobox=839ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-121MS` (url=267ms, nekobox=861ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-211MS` (url=578ms, nekobox=893ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-495MS` (url=5193ms, nekobox=3112ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-107MS` (url=791ms, nekobox=315ms, status=yes)
11. `AKUN-013-CLOUDFLARE-VLESS-WS-113MS` (url=261ms, status=HTTP 204)
12. `AKUN-016-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-634MS` (url=1056ms, status=HTTP 204)
13. `AKUN-017-CLOUDFLARE-VLESS-WS-324MS` (url=1692ms, status=HTTP 204)
14. `AKUN-018-CLOUDFLARE-VLESS-WS-108MS` (url=223ms, status=HTTP 204)
15. `AKUN-019-CLOUDFLARE-VLESS-WS-132MS` (url=931ms, status=HTTP 204)
16. `AKUN-020-TW-CLOUD-VLESS-WS-338MS` (url=5112ms, status=HTTP 204)
17. `AKUN-021-CLOUDFLARE-VLESS-WS-127MS` (url=796ms, status=HTTP 204)
18. `AKUN-023-CLOUDFLARE-VLESS-WS-829MS` (url=255ms, status=HTTP 204)
19. `AKUN-028-UNKNOWN-VLESS-WS-512MS` (url=1292ms, status=HTTP 204)
20. `AKUN-029-CLOUDFLARE-VLESS-WS-752MS` (url=657ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
