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
1. `AKUN-001-008500-VLESS-WS-118MS` (url=285ms, nekobox=274ms, status=yes)
2. `AKUN-002-GOV-VLESS-WS-111MS` (url=283ms, nekobox=296ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-123MS` (url=303ms, nekobox=5157ms, status=no)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-123MS` (url=289ms, nekobox=5157ms, status=no)
5. `AKUN-003-CLOUDFLARE-VLESS-WS-104MS`
6. `AKUN-007-CLOUDFLARE-VLESS-WS-105MS` (url=271ms, nekobox=225ms, status=no)
7. `AKUN-004-UNKNOWN-VLESS-WS-130MS`
8. `AKUN-009-CLOUDWEBMANAGE-EU-FR-VLESS-WS-134MS` (url=308ms, nekobox=5157ms, status=no)
9. `AKUN-010-CLOUDFLARE-VLESS-WS-133MS` (url=294ms, nekobox=5157ms, status=no)
10. `AKUN-005-CLOUDFLARE-VLESS-WS-118MS`
11. `AKUN-006-CLOUDFLARE-VLESS-WS-131MS`
12. `AKUN-007-CLOUDFLARE-VLESS-WS-134MS`
13. `AKUN-014-CLOUDFLARE-VLESS-WS-132MS` (url=308ms, nekobox=5157ms, status=no)
14. `AKUN-008-CLOUDFLARE-VLESS-WS-114MS`
15. `AKUN-009-CLOUDFLARE-VLESS-WS-109MS`
16. `AKUN-017-CLOUDFLARE-VLESS-WS-123MS` (url=246ms, nekobox=5157ms, status=no)
17. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-178MS`
18. `AKUN-019-EE-WELCOMEHOST-20190515-VLESS-WS-118MS` (url=344ms, status=HTTP 204)
19. `AKUN-020-CONFLU-VLESS-WS-334MS` (url=637ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-338MS` (url=671ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-324MS` (url=672ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-111MS` (url=273ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-378MS` (url=696ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-353MS` (url=715ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-130MS` (url=267ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
